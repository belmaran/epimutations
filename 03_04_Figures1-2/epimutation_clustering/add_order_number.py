import sys
file=open(sys.argv[1],"r")

chr="I"
count=0
for line in file:

	line=line.rstrip("\n")
	splitline=line.split("\t")	
	count=count+1
	if splitline[0] != chr:
		count=count+1
		chr=splitline[0]
	print(splitline[0]+"\t"+splitline[1]+"\t"+str(count))

file.close()

		
