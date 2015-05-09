import random
fileOut = open("vectorList.txt", 'w')

def component():
    return random.randrange(0, 1000000)

for i in range(20000):
    writeStr = ""
    writeStr = writeStr + str(component()) + " " + str(component()) + "_" + "\n"
    fileOut.write(writeStr)
fileOut.close() 