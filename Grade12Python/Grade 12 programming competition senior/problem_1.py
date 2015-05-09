def noZeros():
    for element in costArray:
        if element == 0:
            return False
    return True

def removeElement():
    while(noZeros() == False):
        for elementIndex in range(len(costArray)):
            if costArray[elementIndex] == 0:
                costArray.pop(costArray.index(0) - 1)
                costArray.pop(costArray.index(0))
                break

numberIter = input()
costArray = []
for i in range(numberIter):
    currentNum = input()
    costArray.append(currentNum)
        
removeElement()
            



totalCost = 0
for element in costArray:
    totalCost += element
    
print totalCost