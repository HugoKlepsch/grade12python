import random

def insertionSort(origList):
    sortedlist = []
    firstTime = True
    for origIndex in range(len(origList)):
        todo = origList[origIndex]
        if (firstTime):
            sortedlist.insert(0, todo)
            firstTime = False
        else:
            listLen = len(sortedlist)
            for newindex in range(listLen):
                if (newindex != listLen -1):
                    if (todo < sortedlist[newindex]):
                        sortedlist.insert(newindex, todo)
                        break
                else:
                    
                    if (todo < sortedlist[newindex]):
                        sortedlist.insert(newindex, todo)
                        break
                    else:
                        sortedlist.append(todo)
                        break
    return sortedlist


def insertionSortKey(origList, key):
    sortedList = []
    sortedList.append(origList[0]) # If theres nothing in the list, put it in there, 
    del origList[0] #so we dont use it agian
    for star in origList:
        todo = (star[key]) 
        listLen = len(sortedList)
        for newindex in range(listLen):
            comparator = ((sortedList[newindex])[key])
            if (newindex != listLen - 1):
                if (todo < comparator):
                    sortedList.insert(newindex, star)
                    break
            else:
                
                if (todo < comparator):
                    sortedList.insert(newindex, star)
                    break
                else:
                    sortedList.append(star)
                    break
    return sortedList

def mergeSort(origList,key):
    result = []
    if len(origList) < 2:
        return origList
    mid = int(len(origList) / 2)
    y = mergeSort(origList[:mid], key)
    z = mergeSort(origList[mid:], key)
    indexI = 0
    indexJ = 0
    if key != -1:
        while ((indexI < len(y) and (indexJ < len(z)))):
            if y[indexI][key] > z[indexJ][key]:
                result.append(z[indexJ])
                indexJ += 1
            else:
                result.append(y[indexI])
                indexI += 1
        result += y[indexI:]
        result += z[indexJ:]
        return result
    else:
        while ((indexI < len(y) and (indexJ < len(z)))):
            if y[indexI] > z[indexJ]:
                result.append(z[indexJ])
                indexJ += 1
            else:
                result.append(y[indexI])
                indexI += 1
        result += y[indexI:]
        result += z[indexJ:]
        return result
               

def bubbleSort(origList):
    count = 0
    while(isSorted(origList) == False):
        count += 1
        for index in range(len(origList)):
            if (index < len(origList) - 1):
                if (origList[index] > origList[index + 1]):
                    temp = origList[index]
                    origList[index] = origList[index + 1]
                    origList[index + 1] = temp
                    break
    return origList
                


def isSorted(origList):
    for num in range(len(origList) - 1):
        if (num < len(origList) - 1):
            if origList[num] > origList[num+1]:
                return False
    return True
            
# randoList = []
# for i in range (20):
#     randoList.append(random.randrange(0, 50))
# randoList = [10, 46, 48, 13, 45, 42, 24, 43, 1, 49, 13, 37, 27, 29, 5, 46, 29, 21, 43, 20]
# randoList = [41, 17, 6, 15, 26, 25, 8, 20, 31, 47, 44, 37, 39, 31, 43, 23, 2, 0, 41, 11]
# newlist = insertionSort(randoList)
# 
# print newlist
# print isSorted(newlist)
#print bubbleSort(randoList)