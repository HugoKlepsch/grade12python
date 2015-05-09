from Tkinter import *
import HugoSortStars
import searching
import time
import random

#example comment header
'''
Description: 
Params:
Returns:
'''

'''
							.---. __
				 ,		   /     \   \	||||
				\\\\	  |O___O |	 | \\||||
				\   //	  | \_/  |	 |  \   /
				 '--/----/|	    /	 |   |-'
						// //  /    -----'
					   //  \\ /	   /
					  //  // /	  /
					 //  \\ /    /
					//  //      /
				   /|   ' /	   /
				   //\___/	  /
				  //   ||\	 /
				  \\_  || '---'
				  /' /  \\_.-
				 /  /	--| |
				 '-'	  |  |
						   '-'
						 


										.---. __
							 ,		 /	 \   \	||||
							\\\\	  |O___O |	| \\||||
							\   //	| \_/  |	|  \   /
							 '--/----/|	 /	 |   |-'
									// //  /	 -----'
								   //  \\ /	  /
								  //  // /	  /
								 //  \\ /	  /
								//  // /	  /
							   /|   ' /	  /
							   //\___/	  /
							  //   ||\	 /
							  \\_  || '---'
							  /' /  \\_.-
							 /  /	--| |
							 '-'	  |  |
									   '-'
'''



fileOutStars = open("sortedListStars.txt", 'w') #file to write the starsList list. 
fileOutConstallations = open("sortedListConstellation.txt", 'w') #file to write the starConstallationList list.

global starsList #list of lists, each entry is a list containing data for each star
global starConstallationList #list of lists, each entry is a list containing data for each star with a name
global width #pixel width of the canvas, needed global because of button callback limitations
global height #pixel height of the canvas, needed global because of button callback limitations
global lastStarSelected

def readFile(filename):
    fileIn = open(filename)
    
    starsList = []
    starConstallationList = []
    for starLine in fileIn: #each star is on a new line, so 
        starInfo = []
        #starPosList = []
        constalationNameList = []
        elements = starLine.split(" ", 6)
        starInfo.append(float(elements[0])) #x coord
        starInfo.append(float(elements[1])) #y coord
        starInfo.append(float(elements[3])) #henry drapea
        starInfo.append(float(elements[4])) #luminocity intensity
        starInfo.append(float(elements[5])) #harvard revised number
        if (len(elements) > 6): #if there are names /.sixth element
            elements[6] = elements[6].strip("\n")
            constalationNameList = elements[6].split("; ") 
            for starConstInfoList in makeStarConstelationListLine(starInfo, constalationNameList):
                starConstallationList.append(starConstInfoList)
        starInfo.append(constalationNameList)
        starsList.append(starInfo) # add specific info to the star list collection
        
    return starsList, starConstallationList

def makeStarConstelationListLine(starConstInfoList, constalationNameList):
    starConstList = []
    for name in constalationNameList:
        temp = starConstInfoList[ : ]
        temp.append(name)
        starConstList.append(temp)
    return starConstList
        
def findXYConst(starList, starName):
    newStarList = starList[:]
    starIndex = searching.binarySearch(newStarList, starName, 5, False)
    xcoord = starList[starIndex][0]
    ycoord = starList[starIndex][1]
    return [xcoord, ycoord]


def graphConst(constellationName, colour):
    global starConstallationList
    global width
    global height
    constelationFile = open(constellationName)
    for starComboLine in constelationFile:
#         print starComboLine
        starComboLine = starComboLine.strip()
        starComboList = starComboLine.split(",")
        xList = []
        yList = []
        for starName in starComboList:
#             print starName
            xyList = findXYConst(starConstallationList, starName)
#             print xyList
            xyList = calcPixel(xyList[0], xyList[1], width, height)
            xList.append(xyList[0])
            yList.append(xyList[1])
        cv.create_line(xList[0], yList[0], xList[1], yList[1], fill = colour, width=2, tags="lines")
        cv.update()


def clickCallBack(event):
	global starsList
	global lastStarSelected
	if lastStarSelected != None:
		cv.itemconfig(lastStarSelected, fill = 'white')
	clickX = event.x
	clickY = event.y
	closestStar = cv.find_closest(clickX, clickY)
	lastStarSelected = closestStar
	tags = cv.gettags(closestStar)
# 	print closestStar[0]
	cv.itemconfig(closestStar, fill = "red")
	index = int(tags[0])
	star = starsList[index]
	if len(star[5]) != 0:
		infoNameStrVar.set("Name: " + str(star[5]))
	else:
		infoNameStrVar.set("Name: No Name")
	infoPositionStrVar.set("X: " + str(star[0]) + " Y: " + str(star[1]))
	infoHenryStrVar.set("Henry Number: " + str(star[2]))
	infoMagnitudeStrVar.set("Brightness Magnitude: " + str(star[3]))
	infoHarvardStrVar.set("Harvard Revised Number: " + str(star[4]))
		
	
def graphStars(starsList, w, h):
	count = -1
	for star in starsList:
		count +=1
		starX = star[0]
		starY = star[1]
		starMag = star[3] #light magnitude
		xY = calcPixel(starX, starY, w, h)
		
		cv.create_oval(xY[0], xY[1], xY[0] + starMag, xY[1] + starMag, fill = "white", tags=str(count))
	    
def calcPixel(xComp, yComp, w, h): 
    #xaxis f'n: y = (w/2)xComp + (w/2)
    #yaxis f'n: y = (h/2)xComp + (h/2)
    halfW = w / 2
    halfH = h / 2
    xPix = (halfW * xComp) + halfW
#     xPix = (halfH * xComp) + halfH
    yPix = (halfH * yComp * (-1)) + halfH
    return [xPix, yPix]


def sortAndGraph(userList, type):
    if (type == -1): # nosorting
        graphStars(userList, width, height)
    elif (type == 2): #sorting by Y
        newList = HugoSortStars.insertionSortKey(userList, 1)
        graphStars(newList, width, height)
    elif (type == 3): #sorting by X
        newList = HugoSortStars.insertionSortKey(userList, 0)      
        graphStars(newList, width, height)
    elif (type == 4): # sorting my magnitude
        newList = HugoSortStars.insertionSortKey(userList, 3)      
        graphStars(newList, width, height)
    
def drawButtCallBack():
    allList = ["Big Dipper.txt", "Cassiopeia.txt", "Cygnet.txt", "Bootes.txt", "Gemini.txt", "Hydra.txt", "Ursamajor.txt", "Ursaminor.txt"]
    constColorDict = {"Big Dipper.txt":"white", "Cassiopeia.txt":"blue", "Cygnet.txt":"red", "Bootes.txt":"yellow", "Gemini.txt":"green", "Hydra.txt":"orange", "Ursamajor.txt":"brown", "Ursaminor.txt":"pink"}
    selectedConst = constelationStrVar.get() + ".txt"
    if selectedConst == "All.txt":
        for constelation in allList:
            graphConst(constelation, constColorDict[constelation])
    else:
        graphConst(selectedConst, constColorDict[selectedConst])
    
    
def clearButtCallBack():
	cv.delete('lines')
    
width = 710.0
height = 710.0
lastStarSelected = None

root = Tk()

root.wm_title("Starry Sky -- Hugo")
mf = Frame(root)
buttFrame = Frame(root)

infoFrame = LabelFrame(buttFrame, text="Information on selected star")
infoNameStrVar = StringVar()
infoNameStrVar.set(" ")
infoName = Label(infoFrame, textvariable=infoNameStrVar)
infoPositionStrVar = StringVar()
infoPositionStrVar.set(" ")
infoPosition = Label(infoFrame, textvariable=infoPositionStrVar)
infoHenryStrVar = StringVar()
infoHenryStrVar.set(" ")
infoHenry = Label(infoFrame, textvariable=infoHenryStrVar)
infoMagnitudeStrVar = StringVar()
infoMagnitudeStrVar.set(" ")
infoMagnitude = Label(infoFrame, textvariable=infoMagnitudeStrVar)
infoHarvardStrVar = StringVar()
infoHarvardStrVar.set(" ")
infoHarvard = Label(infoFrame, textvariable=infoHarvardStrVar)

cv = Canvas(mf, width = width, height = height, bg = "black")
drawButton = Button(buttFrame, text = "Draw Constellation", command=drawButtCallBack)
clearButton = Button(buttFrame, text = "Clear", command=clearButtCallBack)
constelationStrVar = StringVar()
constelationStrVar.set("All")
constelationMenu = OptionMenu(buttFrame, constelationStrVar, "All", "Big Dipper", "Bootes", "Cassiopeia", "Cygnet", "Gemini", "Hydra", "Ursamajor", "Ursaminor")

 
mf.grid(row = 0, column = 0)
buttFrame.grid(row = 0, column = 1)
infoFrame.grid()
infoName.grid()
infoPosition.grid()
infoHenry.grid()
infoMagnitude.grid()
infoHarvard.grid()
drawButton.grid()
clearButton.grid()
constelationMenu.grid()
cv.grid()

starsList, starConstallationList = readFile("stars.txt")

starConstallationList = HugoSortStars.mergeSort(starConstallationList, 5)


sortAndGraph(starsList, -1)

 
for line in starsList:
    fileOutStars.write(str(line))
    fileOutStars.write('\n')
fileOutStars.close()

for line in starConstallationList:
    fileOutConstallations.write(str(line))
    fileOutConstallations.write('\n')
fileOutConstallations.close()



 


cv.bind("<Button-1>", clickCallBack)

root.mainloop()