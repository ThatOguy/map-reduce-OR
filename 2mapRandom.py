#Orion Radford - Python map/reduce scripts Assignment
#code from Denise Case @ https://github.com/denisecase/python-map-reduce/blob/master/words

import sys 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopWords = set(stopwords.words('english'))

# for each line, reverse
for line in sys.stdin:
  strList = line.strip().split('\t')
  if not strList in stopWords:
      if (len(strList) == 2):
        key, value = strList
        # print(value,'\t',key)
        # right justify using 8 columns - sorting done automatically
        print(value.strip().zfill(8),'\t',key)