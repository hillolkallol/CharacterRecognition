import sys
import numpy as np
import cv2
import os

# MIN_CONTOUR_AREA = 100

RESIZED_IMAGE_WIDTH = 500
RESIZED_IMAGE_HEIGHT = 500

def main():
    for x in range(1, 2):
        for y in range(1, 2):
            if (x < 10):
                if(y < 10):
                    filename = 'Img/Sample00' + str(x) + '/img00' + str(x) + '-00' + str(y) + ".png"
                else:
                    filename = 'Img/Sample00' + str(x) + '/img00' + str(x) + '-0' + str(y) + ".png"
            else:
                if(y < 10):
                    filename = 'Img/Sample0' + str(x) + '/img0' + str(x) + '-00' + str(y) + ".png"
                else:
                    filename = 'Img/Sample0' + str(x) + '/img0' + str(x) + '-0' + str(y) + ".png"
            # print(filename)

            imgTrainingNumbers = cv2.imread('img045-010.png')

            if imgTrainingNumbers is None:
                print ("error: image not read from file \n\n")
                os.system("pause")
                return

            imgGray = cv2.cvtColor(imgTrainingNumbers, cv2.COLOR_BGR2GRAY)
            # imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)
            imgThresh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            imgThreshCopy = imgThresh.copy()

            imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # print(len(npaContours[0][:]))

            maximum = 0
            index = 0
            for npaContour in npaContours:
                if(maximum<len(npaContour)):
                    maximum = len(npaContour)
                    break
                index = index + 1

            # print(index)

            rect = cv2.minAreaRect(npaContours[index])
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            W = rect[1][0]
            H = rect[1][1]

            Xs = [i[0] for i in box]
            Ys = [i[1] for i in box]
            x1 = min(Xs)
            x2 = max(Xs)
            y1 = min(Ys)
            y2 = max(Ys)

            angle = rect[2]
            if angle < -45:
                angle += 90

            if abs(angle) <= 12 or abs(angle) >= 20:
                angle = 0

            # Center of rectangle in source image
            center = ((x1 + x2) / 2, (y1 + y2) / 2)
            # Size of the upright rectangle bounding the rotated rectangle
            size = (x2 - x1, y2 - y1)
            M = cv2.getRotationMatrix2D((size[0] / 2, size[1] / 2), angle, 1)
            # Cropped upright rectangle
            cropped = cv2.getRectSubPix(imgGray, size, center)
            cropped = cv2.warpAffine(cropped, M, size,
                                     flags=cv2.INTER_LINEAR,
                                     borderMode=cv2.BORDER_REPLICATE)
            croppedW = H if H > W else W
            croppedH = H if H < W else W
            # Final cropped & rotated rectangle
            # croppedRotated = cv2.getRectSubPix(cropped, (int(croppedW), int(croppedH)),
            #                                    (size[0] / 2, size[1] / 2))

            imgROIResized = cv2.resize(cropped, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            resized_bw = cv2.threshold(imgROIResized, 128, 255, cv2.THRESH_BINARY)[1]
            cv2.imwrite('img045-010-output.png', resized_bw)
            cv2.imshow("imgROIResized", resized_bw)

    cv2.destroyAllWindows()
    return
if __name__ == "__main__":
    main()
