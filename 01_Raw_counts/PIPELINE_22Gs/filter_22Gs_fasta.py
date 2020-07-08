import sys
file=open(sys.argv[1],"r")
for line in file:
          line=line.rstrip("\n")
          if line.startswith(">"):
              id=line
          else:
              if line.startswith("G") and len(line)==22:
                  print id
                  print line
file.close()
