import sys
file=open(sys.argv[1],"r")
for line in file:
    line=line.rstrip("\n")
    line=line.replace('"','')
    for letter in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]:
        line=line.rstrip(letter)
    print line
file.close()
