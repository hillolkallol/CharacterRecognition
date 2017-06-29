import cv2
import os

RESIZED_IMAGE_WIDTH = 100
RESIZED_IMAGE_HEIGHT = 100

def main():
            imgTrainingNumbers = cv2.imread('letters3.png')

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

            azarray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            subfolder = ['upper', 'lower']

            for i in range(0, 1):
                for j in range(0, 26):
                    for k in range(1, 2):
                        filename = 'new/' + str(subfolder[i]) + '/' + str(azarray[25-j]) + '/' + str(k)
                        print(filename)
                        [intX, intY, intW, intH] = cv2.boundingRect(npaContours[j])

                        cv2.rectangle(imgTrainingNumbers,(intX, intY),(intX + intW, intY + intH),(0, 0, 255), 2)

                        imgROI = imgGray[intY:intY + intH, intX:intX + intW]
                        imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH,RESIZED_IMAGE_HEIGHT))

                        # cv2.imshow("imgROI", imgROI)
                        cv2.imshow("imgROIResized", imgROIResized)

                        cv2.imwrite(filename + '.png', imgROIResized)
                        intChar = cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

if __name__ == "__main__":
    main()
    # end if