__author__ = 'Raj'

from math import radians
from math import sin
from math import tan
from math import cos
from math import sqrt
from math import atan2
from math import log10

def distance(lat1, lon1, lat2, lon2):
          lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
          dlon = lon2 - lon1
          dlat = lat2 - lat1
          a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
          c = 2 * atan2(sqrt(a), sqrt(1-a))
          meters = 6367 * c * 1000
          return meters

inputFile = open("insector_rssi_data_hw2-2.dat",'r')
outFile = open("insector_Output_Log",'w')
outFile.write("Distance(m)"+" "+"RSSI(dBm)"+"\n")
readData = inputFile.readline()
for line in inputFile:
    val = line.split(" ")
    dist = str(log10(distance(float(40.916309),float(-73.124071),float(val[0]),float(val[1]))))
    outFile.write(dist+" "+val[2])
inputFile.close()
outFile.close()