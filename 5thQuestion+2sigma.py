__author__ = 'Raj'

inputFile = open("insector_Output.txt",'r')
outFile = open("insector_Output_+2sigma",'w')
outFile.write("Distance(m)"+" "+"RSSI(dBm)+2sigma(10.84867681)"+" "+"RSSI(dBm)"+"\n")
readData = inputFile.readline()
for line in inputFile:
    val = line.split(" ")
    rssiPlusSigma = str(float(val[1])+(2*10.84867681))
    outFile.write(val[0]+" "+rssiPlusSigma+" "+val[1])
inputFile.close()
outFile.close()