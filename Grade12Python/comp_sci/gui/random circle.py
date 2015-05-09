from Tkinter import *   
from math import *
from random import *
def getRandomXY():
    xy = []
    for i in range (2):
        xy.append(randint(0, 400))
    return xy
def getColour():
    val = colourRad.get()
    if val == 0:
        return "white"
    elif val == 1:
        return "red"
    elif val == 2:
        return "blue"
    elif val == 3:
        return "yellow"
    elif val == 4:
        return "green"
def getSize():
    small = 30
    med = 90
    big = 140
    val = sizeRad.get()
    if val == 0:
        return small
    elif val == 1:
        return med
    elif val == 2:
        return big
def drawCircle():
    xy = getRandomXY()
    colour = getColour()
    size = getSize()
    cv.create_oval(xy[0], xy[1], xy[0] + size, xy[1] + size, fill = colour, tag = 1)
def clear():
    cv.delete('all')
#frame
poot = Tk()
colourRad = IntVar()
sizeRad = IntVar()
mf = Frame(poot, bg = "#99CC00", relief = RAISED)
cFrame = LabelFrame(mf, text = "choose colour: ", bg = "#CCFF00", relief = RAISED)
sFrame = LabelFrame(mf, text = "choose size: ", bg = "#CCFF00", relief = RAISED)
bcFrame = LabelFrame(mf, text = "choose background colour:", bg = "#CCFF00", relief = RAISED)
cv = Canvas(mf, width = 400, height = 400, bg = "black")
#widget
whiteButt = Radiobutton(cFrame, text = "White", variable = colourRad, value = 0, bg = "white")
redButt = Radiobutton(cFrame, text = "Red", variable = colourRad, value = 1, bg = "red")
blueButt = Radiobutton(cFrame, text = "Blue", variable = colourRad, value = 2, bg = "blue")
YellowButt = Radiobutton(cFrame, text = "Yellow", variable = colourRad, value = 3, bg = "yellow")
GreenButt = Radiobutton(cFrame, text = "Green", variable = colourRad, value = 4, bg = 'green')
smallButt = Radiobutton(sFrame, text = "Smole", variable = sizeRad, value = 0, font = ("Ubuntu", 12))
medButt = Radiobutton(sFrame, text = "Medium", variable = sizeRad, value = 1, font = ("Ubuntu", 20))
bigButt = Radiobutton(sFrame, text = "Big", variable = sizeRad, value = 2, font = ("Ubuntu", 30))
goButt = Button(mf, text = "GO!", command = drawCircle, height = 5, width = 20)
clearButt = Button(mf, text = "Clear", command = clear)        
#grdi dat wdigts
mf.grid()
cFrame.grid(row = 1, column = 1, padx = 20)
sFrame.grid(row = 2, column = 1, padx = 20)
bcFrame.grid(row = 3, column = 1, padx = 20)
cv.grid(row = 1, column = 2, padx = 20, pady = 20)
whiteButt.grid(row = 1, column = 1, padx = 4, pady = 4, sticky = W)
redButt.grid(row = 2, column = 1,  padx = 4, pady = 4, sticky = W)
blueButt.grid(row = 3,column = 1,  padx = 4, pady = 4, sticky = W)
YellowButt.grid(row = 4, column = 1,  padx = 4, pady = 4, sticky = W)
GreenButt.grid(row = 5, column = 1,  padx = 4, pady = 4, sticky = W)
smallButt.grid(row = 1, column = 1,  padx = 4, pady = 4, sticky = W)
medButt.grid(row = 2, column = 1,  padx = 4, pady = 4, sticky = W)
bigButt.grid(row = 3, column = 1,  padx = 4, pady = 4, sticky = W)
goButt.grid(row = 2, column = 2, padx = 20, pady = 10)
clearButt.grid(row = 5, column = 2, padx = 20, pady = 20)
poot.mainloop()
