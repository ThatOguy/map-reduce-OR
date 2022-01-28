in02 = open("out01OR.txt","r")  # open file, read-only
out02 = open("out02OR.txt", "w") # open file, write
lines = in02.readlines()
lines.sort()

for line in lines:
	out02.write(line)

in02.close()
out02.close()
