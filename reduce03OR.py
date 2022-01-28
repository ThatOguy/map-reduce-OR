in03 = open("out02OR.txt","r")
out03 = open("out03OR.txt", "w")

thisKey = ""
thisValue = 0.0

for line in in03:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      out03.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
out03.write(thisKey + '\t' + str(thisValue)+'\n')

in03.close()
out03.close()