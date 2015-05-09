import math
import random
import HugoSortStars

def linearSearch(userList, key):
    count = 0
    listLen = len(userList)
    for index in range(listLen):
        count += 1
        if (userList[index] == key):
            print "iterations: ", count
            print "Worst Case: ", listLen
            return index
    return -1

def binarySearch(userList, searchTerm, key, testEstimate):
    firstInd = 0
    listLen = len(userList)
    lastInd = listLen - 1
    keepGoing = True
    count = 0
    if (testEstimate):
        while (firstInd <= lastInd):
            count += 1
            midpoint = (firstInd + lastInd) // 2
            if userList[midpoint] == searchTerm:
                print "Iterations: ", count
                print "log(", listLen, ") = ", (float(math.log(listLen)) / math.log(2))
                #return midpoint
                return [count, (float(math.log(listLen)) / math.log(2))]
            else:
                if searchTerm < userList[midpoint]:
                    lastInd = midpoint-1
                else:
                    firstInd = midpoint+1
        return -1
    else:
        if key == -1:
            while (firstInd <= lastInd):
                count += 1
                midpoint = (firstInd + lastInd) // 2
                if userList[midpoint] == searchTerm:
#                      print "Iterations: ", count
#                      print "log(", listLen, ") = ", (float(math.log(listLen)) / math.log(2))
                     return midpoint
                    #return [midpoint, count, (float(math.log(listLen)) / math.log(2))]
                else:
                    if searchTerm < userList[midpoint]:
                        lastInd = midpoint-1
                    else:
                        firstInd = midpoint+1
            return -1
        else:
            while (firstInd <= lastInd):
                count += 1
                midpoint = (firstInd + lastInd) // 2
                if userList[midpoint][key] == searchTerm:
#                      print "Iterations: ", count
#                      print "log(", listLen, ") = ", (float(math.log(listLen)) / math.log(2))
                     return midpoint
                    #return [midpoint, count, (float(math.log(listLen)) / math.log(2))]
                else:
                    if searchTerm < userList[midpoint][key]:
                        lastInd = midpoint-1
                    else:
                        firstInd = midpoint+1
            return -1

def makeList(length, min,max):
    randlist = []
    for i in range(length):
        randlist.append(random.randint(min, max))
    return HugoSortStars.insertionSort(randlist)

def checkBinarysortLengthEstimate():
    listList = []
    
    for i in range(2, 2000):
        listList.append(makeList(i, -1000, 1000))
                        
    for i in listList:
        key = i[0, random.randint(0, len(i) - 1)]
        result = binarySearch(i, key, True)
        if (result != -1):
            if (result[0] > (result[1] + 1)):
                print "fail"
    print "done"
    

# newStarList = [[1, 2, 3, 4, 5, "aong"], [2, 2, 4, 7, 6, "bing"], [1, 2, 3, 4, 7, "crabble"], [1, 2, 3, 4, 8, "dhingle"], [1, 2, 3, 4, 9, "eraham"]]
# starName = "aong"
# starIndex = binarySearch(newStarList, starName, 5, False)
# 
# 
# print starIndex