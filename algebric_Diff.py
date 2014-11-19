__author__ = 'Raj'

inputFile = open("insector_Output.txt",'r')
outFile = open("insector_Output_alegebric.txt",'w')
outFile.write("Distance(m)"+" "+"deviation"+"\n")
readData = inputFile.readline()
for line in inputFile:
    val = line.split(" ")
    dist = str((float(val[1]))-((-0.0188*(float(val[0])))-69.693))
    outFile.write(val[0]+" "+dist)
    outFile.write("\n")
inputFile.close()
outFile.close()