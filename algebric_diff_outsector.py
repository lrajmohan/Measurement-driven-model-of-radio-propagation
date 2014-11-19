__author__ = 'Raj'

inputFile = open("outsector_Output",'r')
outFile = open("outsector_Output_alegebric.txt",'w')
outFile.write("Distance(m)"+" "+"deviation"+"\n")
readData = inputFile.readline()
for line in inputFile:
    val = line.split(" ")
    dist = str((float(val[1]))-((-0.0521*(float(val[0])))-66.16))
    outFile.write(val[0]+" "+dist)
    outFile.write("\n")
inputFile.close()
outFile.close()