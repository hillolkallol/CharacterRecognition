import numpy as np
import os, os.path

def to_pattern(letter):
    from numpy import array
    return array([+1 if c=='1' else -1 for c in letter.replace('\n','')])

def display(pattern):
    from pylab import imshow, cm, show
    imshow(pattern.reshape((100,100)),cmap=cm.binary, interpolation='nearest')
    show()

def train(patterns):
    from numpy import zeros, outer, diag_indices
    r,c = patterns.shape
    W = zeros((c,c))
    for p in patterns:
        W = W + outer(p,p)
    W[diag_indices(c)] = 0
    return W/r

def synchronousTesting(W, sPatterns):
    from numpy import vectorize, dot
    sgn = vectorize(lambda x: -1 if x<0 else +1)
    oldPatterns = sPatterns
    while(True):
        sPatterns = sgn(dot(sPatterns, W))
        if(np.all(sPatterns == oldPatterns)):
            break
        oldPatterns = sPatterns
    return sPatterns

def asynchronousTesting(W, asPatterns):
    from numpy import vectorize, dot
    import random
    sgn = vectorize(lambda x: -1 if x<0 else +1)
    xPatterns = asPatterns
    yPatterns = asPatterns
    randomNumber = random.sample(range(0,len(yPatterns)), len(yPatterns))

    for x in range(0, len(randomNumber)):
        yPatterns[randomNumber[x]] = sgn(xPatterns[randomNumber[x]] + dot(yPatterns, W[:][randomNumber[x]]))
        # print(yPatterns[randomNumber[x]])
    return yPatterns

# def hopfield_energy(W, hEPatterns):
#     from numpy import array, dot
#     return array([-0.5*dot(dot(p.T,W),p) for p in hEPatterns])

def main():
    from numpy import array
    azarray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    subfolder = ['upper', 'lower']

    patterns = np.empty((0, 10000))
    for i in range(0, 1):
        for j in range(9,19):
            items = len([name for name in os.listdir('dataset/' + str(subfolder[i]) + '/' + str(azarray[j]))
                 if name.endswith('.txt') and os.path.isfile(os.path.join('dataset/' + str(subfolder[i]) + '/' + str(azarray[j]), name))])

            for k in range(0,1):
                # filename_input = 'training/' + str(subfolder[i]) + '/' + str(azarray[j]) + '/' + str(k)
                filename = 'dataset/' + str(subfolder[i]) + '/' + str(azarray[j]) + '/' + str(k)
                print(filename)
                try:
                    letter = open(filename + '.txt').read()
                except:
                    print('****** Exception! ******')
                    pass
                letter = letter.replace(' ', '')
                # display(to_pattern(letter))
                patterns = np.append(patterns, [to_pattern(letter)], axis=0)

    # Testing input
    azarraytesting = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    subfoldertesting = ['upper', 'lower']
    testingPatterns = np.empty((0, 10000))
    for ii in range(0, 1):
        for jj in range(9, 19):
            items = len([name for name in os.listdir('dataset/' + str(subfoldertesting[ii]) + '/' + str(azarraytesting[jj]))
                 if name.endswith('.txt') and os.path.isfile(os.path.join('dataset/' + str(subfoldertesting[ii]) + '/' + str(azarraytesting[jj]), name))])

            for kk in range(0, 1):
                # filename_input = 'training/' + str(subfolder[i]) + '/' + str(azarray[j]) + '/' + str(k)
                testfilename = 'dataset/' + str(subfoldertesting[ii]) + '/' + str(azarraytesting[jj]) + '/' + str(kk)
                print(testfilename)
                try:
                    testingLetter = open(testfilename + '.txt').read()
                except:
                    print('****** Exception! ******')
                    pass
                testingLetter = testingLetter.replace(' ', '')
                testingLetter = array([+1 if c=='1' else 0 for c in testingLetter.replace('\n','')])
                # print(testingLetter.reshape((20, 20)))
                testingLetter = testingLetter.reshape((100, 100)) #problem here............
                # for m in range(50, 100):
                #     for n in range(50, 100):
                #         testingLetter[m][n] = 1
                # print(''.join(str(e) for e in testingLetter))
                testingLetter = ''.join(str(e) for e in testingLetter)
                testingLetter = testingLetter.replace('[', '')
                testingLetter = testingLetter.replace(']', '')
                testingLetter = testingLetter.replace(' ', '')
                # print(len(testingLetter))
                # display(to_pattern(testingLetter))
                testingPatterns = np.append(testingPatterns, [to_pattern(testingLetter)], axis=0)

    # try:
    #     testing = open('0.txt').read()
    #     testing = testing.replace(' ', '')
    #     testing = to_pattern(testing)
    # except:
    #     print('****** Exception! ******')
    #     pass
    #
    # testing = testing.reshape((20, 20))
    #
    # for m in range(10, 20):
    #     for n in range(0, 10):
    #         testing[m][n] = -1

    # print(testing)
    # display(testing)
    # print(len(to_pattern(testing)))
    weight = train(patterns)
    for t in range(0, len(testingPatterns)):
    #     display(testingPatterns[0])
    #     display(synchronousTesting(weight, testingPatterns[t]))
        display(asynchronousTesting(weight, testingPatterns[t]))
    # print(hopfield_energy(train(patterns), to_pattern(testing)))

if __name__ == "__main__":
        main()

