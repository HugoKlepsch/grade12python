import math 
fileIn = open("/home/hugo/ownCloud/Homework/gr 12/physics/vector draft/TwoList.txt")
fileOut = open("/home/hugo/ownCloud/Homework/gr 12/physics/vector draft/TwoComponents.txt", "w")
lineList = []
for line in fileIn:
    lineList.append(line)
for i in range(3):    
    lineList.pop(0)
lineListLen = len(lineList)
compListList = []
for vectorIndex in range(lineListLen):
    compList = []
    xComp = 0
    yComp = 0
    dAngleFromRHoriz = 0
    vector = lineList[vectorIndex]
    vectorStrLen = len(vector)
    indexFirst = vector.index(" ")
    indexSecond = vector.index("_")
    magnitude = int(vector[0:indexFirst])
    angle = math.radians(int(vector[indexFirst + 1: indexSecond]))
    dErection = vector[indexSecond + 1 : vectorStrLen - 2]
    if (len(dErection) == 1):
        if (dErection == "N"):
            xComp += magnitude
            dAngleFromRHoriz = 90
        elif (dErection == "S"):
            xComp += (magnitude * -1)
            dAngleFromRHoriz = 180
        elif (dErection == "E"):
            yComp += magnitude
            dAngleFromRHoriz = 0
        elif (dErection == "W"):
            yComp += (magnitude * -1)
            dAngleFromRHoriz = 270
    else:
        if (dErection == "EN"):
            xComp = magnitude * (math.cos(angle))
            yComp = magnitude * (math.sin(angle))
            dAngleFromRHoriz = (math.degrees(math.atan(float(yComp)/float(xComp))))
        elif (dErection == "NE"):
            xComp = magnitude * (math.sin(angle))
            yComp = magnitude * (math.cos(angle))
            dAngleFromRHoriz = 90 - (math.degrees(math.atan(float(xComp)/float(yComp))))
        elif (dErection == "NW"):
            xComp = magnitude * (math.sin(angle))
            yComp = magnitude * (math.cos(angle))
            dAngleFromRHoriz = 90 + (math.degrees(math.atan(float(xComp)/float(yComp))))
            xComp = xComp * -1
        elif (dErection == "WN"):
            xComp = magnitude * (math.cos(angle))
            yComp = magnitude * (math.sin(angle))
            dAngleFromRHoriz = 180 - (math.degrees(math.atan(float(yComp)/float(xComp))))
            xComp = xComp * -1
        elif (dErection == "WS"):
            xComp = magnitude * (math.cos(angle))
            yComp = magnitude * (math.sin(angle))
            dAngleFromRHoriz = 180 + (math.degrees(math.atan(float(yComp)/float(xComp))))
            xComp = xComp * -1
            yComp = yComp * -1
        elif (dErection == "SW"):
            xComp = magnitude * (math.sin(angle))
            yComp = magnitude * (math.cos(angle))
            dAngleFromRHoriz = 270 - (math.degrees(math.atan(float(xComp)/float(yComp))))
            xComp = xComp * -1
            yComp = yComp * -1
        elif (dErection == "SE"):
            xComp = magnitude * (math.sin(angle))
            yComp = magnitude * (math.cos(angle))
            dAngleFromRHoriz = 270 + (math.degrees(math.atan(float(xComp)/float(yComp))))
            yComp = yComp * -1
        elif (dErection == "ES"):
            xComp = magnitude * (math.cos(angle))
            yComp = magnitude * (math.sin(angle))
            dAngleFromRHoriz = 360 - (math.degrees(math.atan(float(yComp)/float(xComp))))
            yComp = yComp * -1
    compList.append(xComp)
    compList.append(yComp)
#     compList.append(dAngleFromRHoriz)
    compListList.append(compList)
    
for list in compListList:
    strangleGraham = ""
    for elementerino in list:
        strangleGraham = strangleGraham + str(elementerino) + " "
    strangleGraham = strangleGraham + "\n"
    fileOut.write(strangleGraham)
    
fileIn.close()
fileOut.close()