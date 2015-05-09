import math

fileIn = open("/home/hugo/ownCloud/Homework/gr 12/physics/vector draft/componentList.txt")
global xList
global yList
xList = []
yList = []

for line in fileIn:
    lineList = line.split()
    xList.append(float(lineList[0]))
    yList.append(float(lineList[1]))
    
    

def calcPos(v1, v2, v3, v4, v5):
    xPos = 0
    yPos = 0
    v1 = v1 - 1
    v2 = v2 - 1
    v3 = v3 - 1
    v4 = v4 - 1
    v5 = v5 - 1
    xPos = xPos + (xList[v1]) + (xList[v2]) + (xList[v3]) + (xList[v4]) + (xList[v5])
    yPos = yPos + (yList[v1]) + (yList[v2]) + (yList[v3]) + (yList[v4]) + (yList[v5])
    return xPos, yPos

def removeUsed(removedList):
    for item in removedList:
        index = choices.index(item)
        choices.pop(index)



removedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]

removeUsed(removedList)


for v1 in choices:
    for v2 in choices:
        for v3 in choices:
            for v4 in choices:
                for v5 in choices:
                    x, y = calcPos(v1, v2, v3, v4, v5)
                    if (x == 0) and (y == 0):
                        print v1, v2, v3, v4, v5
#                     if (v1 == v2) or (v2 == v3) or (v3 == v4) or (v4 == v5):
#                         pass
#                     else:
#                         x, y = calcPos(v1, v2, v3, v4, v5)
#                         if (x == 0) and (y == 0):
#                             print v1, v2, v3, v4, v5
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        