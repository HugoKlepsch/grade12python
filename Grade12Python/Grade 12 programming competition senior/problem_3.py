def countScore():
    count = 0
    for gateInfo in takenList:
        if gateInfo[0] == 1:
            count += 1
    print count
    exit()
    
    
numGates = input()
numPlanes = input()

pList = []
takenList = []
for planeCount in range(numPlanes):
    pList.append(input())
    
takenList.append([0, 0])
for element in range(numGates):
    takenList.append([0, 0])
    
for wantedGateIndex in range(len(pList)):
    planeWanted = pList[wantedGateIndex]
    gatetake = takenList[planeWanted]
    if gatetake[0] == 0:
        gatetake[0] = 1
        gatetake[1] = planeWanted
    else:
        gated = False
        for gateNum in range(planeWanted, 0, -1):
            gateInfo = takenList[gateNum]
            if (gateInfo[0] == 0) and gated == False:
                gateInfo[0] = 1
                gateInfo[1] = pList[wantedGateIndex]
                gated = True
        if gated == False:
            countScore()