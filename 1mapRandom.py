#Orion Radford - Python map/reduce scripts Assignment
#code from Denise Case @ https://github.com/denisecase/python-map-reduce/blob/master/words

import sys 
import re

for line in sys.stdin:
  words = line.strip().lower().split(" ")
  for word in words:
    cleanWord = re.sub('[^a-z]+', '', word)
    print(cleanWord,',',1)