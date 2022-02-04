#Orion Radford - Python map/reduce scripts Assignment
#code from Denise Case @ https://github.com/denisecase/python-map-reduce/blob/master/words

import sys

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    count, word = datalist
    print(count,'\t',word)