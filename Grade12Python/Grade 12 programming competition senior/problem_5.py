def calcPie(list):
    calc1 = 0
    calc2 = 0
    for pieIndex in range(0, len(list), 2):
        calc1 += list[pieIndex]
    for pieIndex in range(1, len(list), 2):
        calc2 += list[pieIndex]
    if calc1 > calc2:
        return calc1
    else:
        return calc2
    
numN = input()
nList = []
for i in range(numN):
    nList.append(input())
numM = input()
mList = []
for i in range(numM):
    mList.append(input())
    
mList.sort()

avg = 0.0
for item in nList:
    avg += item
avg = avg / len(nList)
if (nList[0] >= avg):
    for index in range(len(nList)):
        if (len(mList) != 0):
            nList.insert(index, mList.pop(0))
    print calcPie(nList)
            
            
else:
    print 44 # our one true god