import numpy as np
import cv2

azarray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
subfolder = ['upper', 'lower']

for i in range(0, 1):
    for j in range(22, 23):
        for k in range(5, 6):
            filename = 'new/' + str(subfolder[i]) + '/' + str(azarray[j]) + '/' + str(k)
            # Create a black image
            img = np.zeros((100, 100, 3), np.uint8)
            img[:, :, :] = (255, 255, 255)

            # Write some Text
            font = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
            cv2.putText(img,str(azarray[j]),(5,100), font, 5,(0,0,0),5)

            #Display the image
            # cv2.imshow("img",img)
            # cv2.waitKey(0)

            #Save image
            # cv2.imwrite(filename + '.png', img)