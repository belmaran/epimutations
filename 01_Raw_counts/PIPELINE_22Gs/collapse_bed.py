
import sys

file=open(sys.argv[1],"r")
dict={}

#store in dictionary the number of times a line appears on the dataset
for line in file:
	if line in dict:
		dict[line]=dict[line]+1
	else:
		dict[line]=1

#print the line, replacing the number of reads info by the nb of reads mapped to that specific location
for element in dict:
	el=element.split(",")
	nreads=str(dict[element])
	print el[0]+","+el[1]+","+nreads+","+el[2].rstrip("\n")

	
