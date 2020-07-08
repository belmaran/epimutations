import sys
file=open(sys.argv[1],"r")

for line in file:
	        id=line.rstrip("\r\n")
		line=line.rstrip('"')
		if id.count(".")==2:
			id=id.split(".")[0]+"."+id.split(".")[1]
		for letter in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
			id=id.rstrip(letter)
		print id

file.close()
