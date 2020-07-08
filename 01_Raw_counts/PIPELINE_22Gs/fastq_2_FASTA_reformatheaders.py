import sys

inputstring = sys.argv[1]
infile = open(inputstring,"r")

count=0
for line in infile:
	count = count +1
	if count%4 == 2:
                line=line.rstrip("\n")
                if len(line)>5:
                        print ">"+str(len(line))+","+line[0]+","+line
                        print line

infile.close()

