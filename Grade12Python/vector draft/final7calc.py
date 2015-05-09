import math
  

def calcPos(v1, v2, v3, v4, v5, v6, v7):
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



xList = [0, ]                    
yList = [-11]

print calcPos(1, 2, 3, 4, 5, 6, 7)