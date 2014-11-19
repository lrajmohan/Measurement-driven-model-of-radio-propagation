__author__ = 'Raj'

inputFile = open("outsector_Output",'r')
outFile = open("outsector_Output_+sigma",'w')
outFile.write("Distance(m)"+" "+"RSSI(dBm)+sigma(10.84867681)"+" "+"RSSI(dBm)"+"\n")
readData = inputFile.readline()
for line in inputFile:
    val = line.split(" ")
    rssiPlusSigma = str(float(val[1])+12.9175347)
    outFile.write(val[0]+" "+rssiPlusSigma+" "+val[1])
inputFile.close()
outFile.close()
