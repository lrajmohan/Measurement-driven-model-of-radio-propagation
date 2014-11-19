__author__ = 'Raj'

inputFile = open("insector_Output.txt",'r')
outFile = open("insector_Output_+sigma",'w')
outFile.write("Distance(m)"+" "+"RSSI(dBm)+sigma(12.9175347)"+" "+"RSSI(dBm)"+"\n")
readData = inputFile.readline()
for line in inputFile:
    val = line.split(" ")
    rssiPlusSigma = str(float(val[1])+10.84867681)
    outFile.write(val[0]+" "+rssiPlusSigma+" "+val[1])
inputFile.close()
outFile.close()