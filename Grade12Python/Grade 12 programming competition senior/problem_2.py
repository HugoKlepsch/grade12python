def checkSize(wanted, actual):
    if wanted == "S":
        return True
    elif wanted == "M":
        if actual == "S":
            return False
        else:
            return True
    elif (wanted == "L"):
        if actual == "L":
            return True
        else:
            return False


numJersy = input()
numAthl = input()

jList = []
for jCount in range(numJersy):
    currentJ = raw_input()
    jList.append(currentJ)
aList = []
for aCount in range(numAthl):
    currentA = raw_input()
    aList.append(currentA)

takenList = []
for i in jList:
    takenList.append(0)


for athleteIndex in range(len(aList)):
    line = aList[athleteIndex]
    if takenList[(int(line[2])) - 1] == 0:
        if (checkSize(line[0], jList[(int(line[2])) - 1])):
            takenList[(int(line[2])) - 1] = 1

            
    else:
        pass 
count = 0
for j in takenList:
    if j == 1:
        count += 1
print count