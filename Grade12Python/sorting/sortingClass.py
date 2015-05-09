import math
import HugoSort

def magnitude(xComp, yComp):
    return math.sqrt((xComp ** 2) + (yComp ** 2))

fileIn = open("vectorList.txt")
xCompList = []
yCompList = []
for line in fileIn:
    strLen = len(line)
    endFirst = line.index(" ")
    first = int(line[0:endFirst])
    second = int(line[endFirst + 1:strLen - 2])
    xCompList.append(first)
    yCompList.append(second)
    
# print xCompList
# print yCompList 

magList = []
for index in range(len(xCompList)):
    mag = magnitude(xCompList[index], yCompList[index])
    magList.append(mag)
sortedList = HugoSort.insertionSort(magList)
print sortedList