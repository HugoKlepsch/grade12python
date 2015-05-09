from Tkinter import * 
import time


w = 1366
h = 700
multix = input("enter zoom x: ")
multiy = input("enter zoom y: ")
size = input("enter size of dot: ")

numIter = input("number of iterations to calculate: ")
# multix = numIter * 0.06
# multiy = numIter * 0.01
# size = 1

def sortnumbers(w, x, y, z):
    while((w <= x) == False or (x <= y) == False or (y <= z) == False):
        if (x < w):
            tempvar = w
            w = x
            x = tempvar
        if (y < x):
            tempvar = x
            x = y
            y = tempvar
        if (z < y):
            tempvar = y
            y = z
            z = tempvar
    return w, x, y, z

def howManyBits(number):
    for i in range(62):
        if (2 ** i) > number:
            return i - 1
    
def windchill(temperature):
    chilllist = []
    for velocity in range(0, 40, 5):
        windchillval = 13.12 + (0.6215 * temperature) - (11.37 * (velocity ** 0.16)) + (0.3965 * (temperature * (velocity ** 0.16)))
        chilllist.append(windchillval)
    return chilllist

def collatz(number):
    count = 0
    highest = 0
    while (number != 1):
        count += 1
        if (number > highest):
            highest = number
        if ((number % 2) == 0):
            number = number / 2
        else:
            number = (number * 3) + 1
        xp1 = (count * multix) + 1
        xp2 = xp1 + 1
        yp1 = h-(number * multiy)
        yp2 = yp1 + 1
#         cv.create_rectangle(xp1, yp1, xp2, yp2, fill = "black", outline = "black")
#         cv.update()
    return count, highest





    
 
    
root = Tk()
mf = Frame(root, bg = "#99CC00", relief = RAISED)
cv = Canvas(mf, width = w, height = h, bg = "white")
 
 
mf.grid()
cv.grid()

countlist = []
#cv.create_rectangle(0, h - (dank * multi), w, h - (dank * multi) + 1, fill = "grey")
oldx = 0
oldy = 0
for collatznum in range(2, numIter):
    e, highest = collatz(collatznum)
    countlist.append(e)
    #time.sleep(.01)
    x1 = collatznum * multix
    x2 = x1 + size
    #y1 = h - (e * multiy)
    y1 = h - (highest * multiy)
    y2 = y1 + size
    #cv.create_line(oldx, oldy, x1, y1, fill = "red")
    oldx = x1
    oldy = y1
    
    cv.create_rectangle(x1, y1, x2, y2, fill = "black", outline = "black")
    #cv.update()
    #root.mainloop()
#cv.postscript(file="graph.ps", colormode='color')

#main
# sortedList = sortnumbers(140, 40, 20, 99)
# for i in sortedList:
#     print i
 
# print howManyBits(12314)
# windchilllist = []
# for temperature in range(-10, 40, 5):
#     windchilllist.append(windchill(temperature))
#  
# inittemp = -10
#  
# for temperatureindex in range(len(windchilllist)):
#     for speed in windchilllist[temperatureindex]:
#         cv.create_oval(((speed * 18)), (400 - (inittemp * 18)), ((speed * 18) + 2), (400 - (inittemp * 18) + 2), fill = "black")
#     inittemp = inittemp + 5


root.mainloop()



