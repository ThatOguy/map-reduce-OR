#Orion Radford - Python map/reduce scripts Assignment
#code from Denise Case @ https://github.com/denisecase/python-map-reduce/blob/master/words

import sys 
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

# for each line, reverse
for line in sys.stdin:
  strList = line.strip().split('\t')
  if strList[0] not in stopWords:
    if (len(strList) == 2):
      key, value = strList
      # right justify using 8 columns - sorting done automatically
      print(value.strip().zfill(8),'\t',key)