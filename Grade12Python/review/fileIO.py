

# def loremIpsum():
#     fileIn = open("loremIpsum.txt")
#     commaCount = 0
#     parraCount = 1
#     periodCount = 0
#     articleList = fileIn.read()
#     asciilist = []
#     for char in range (len(articleList)):
#         asciilist.append(ord(articleList[char]))
#     for code in range(len(asciilist)):
#         #print articleList[code], asciilist[code]
#         if (asciilist[code] == 44):
#             commaCount += 1
#         if (asciilist[code] == 10):
#             if ((code + 1) < len(asciilist)):
#                 if (asciilist[code + 1] == 10):
#                     parraCount += 1
#         if (asciilist[code] == 46):
#             periodCount += 1
#     #print asciilist
#     fileIn.close()
#     print commaCount, parraCount, periodCount
#     
#     
#     
# def replace(patternStr, replaceSrt, fileInName, fileOutName):
#     if (fileInName == fileOutName):
#         fileIn = open(fileInName, 'rw')
#         sameFile = True
#     else:
#         fileIn = open(fileInName)
#         fileOut = open(fileOutName, 'w')
#         sameFile = False
#     
#     inList = fileIn.read()
#     inList = inList.split()
#     
#     for wordIndex in range(len(inList)):
#         if (inList[wordIndex] == patternStr):
#             inList[wordIndex] = replaceSrt
#      
#     outStr = ""
#     for word in inList:
#         outStr = outStr + word + " "
#     
#     
#     
#     
#     fileIn.close()
#     if(sameFile == True):
#         fileIn.write(outStr)
#         fileIn.close()
#     else:
#         fileOut.write(outStr)
#         fileIn.close()
#         fileOut.close()
#     print "completed"
           
#replace("ipsum", "Hugo", "loremIpsum.txt", "loremFixdEm.txt")
def testLines(filename):
    fileIn = open(filename)
    fileStr = fileIn.read()
    print fileStr
    
    fileList = fileStr.split('\\n')
    print fileList
    asciiList = []
    for char in range (len(fileStr)):
        asciiList.append(ord(fileStr[char]))
        print asciiList[char], fileStr[char]
#     #price after the ord 202
#     for index in range(len(asciiList)):
#         if (int(asciiList[index]) == 202):
#             pass



testLines("FTSE100.csv")


# print 'comma', loremIpsum()
# print 'parra', loremIpsum()
