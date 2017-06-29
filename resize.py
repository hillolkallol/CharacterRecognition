import sys
import numpy as np
import cv2
import os, os.path
from PIL import Image

RESIZED_IMAGE_WIDTH = 50
RESIZED_IMAGE_HEIGHT = 50

def main():
    azarray = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    subfolder = ['upper','lower']

    # azarray = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # subfolder = 'lu'

    # print(str(azarray[1:3]))
    for i in range(0, 2):
        for j in range(0, 26):
            items = len([name for name in os.listdir('training/' + str(subfolder[i]) + '/' + str(azarray[j]))
                 if name.endswith('.gif') and os.path.isfile(os.path.join('training/' + str(subfolder[i]) + '/' + str(azarray[j]), name))])

            for k in range(0, items):
                filename_input = 'training/' + str(subfolder[i]) + '/' + str(azarray[j]) + '/' + str(k)
                filename_output = 'resized50x50/' + str(subfolder[i]) + '/' + str(azarray[j]) + '/' + str(k)
                print(filename_input)

                try:
                    imgTrainingNumbers = Image.open(filename_input + '.gif')
                except:
                    print('******' + filename_input + '******')
                    pass

                if imgTrainingNumbers is None:
                    print ("error: image not read from file \n\n")
                    os.system("pause")
                    return

                imgGray = imgTrainingNumbers.convert('1')

                imgROIResized = imgGray.resize((RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
                imgROIResized.convert('1')
                os.makedirs(os.path.dirname(filename_output), exist_ok=True)
                imgROIResized.save(filename_output + '.png')

                img = cv2.imread(filename_output + '.png')
                imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                tempFile = open(filename_output + '.txt', 'w')
                for x in imgGray:
                    for y in x:
                        for a in range(0, y.size):
                            if(y == 0):
                                tempFile.write(str(y))
                                tempFile.write(' ')
                            else:
                                tempFile.write(str(1))
                                tempFile.write(' ')
                    tempFile.write('\n')
                tempFile.write('\n')

    cv2.destroyAllWindows()
    return
if __name__ == "__main__":
    main()
