import sys
file=open(sys.argv[1],"r")
for line in file:
    line=line.rstrip("\n")
    splitline=line.split("\t")
    pos=splitline[2]; pos=pos.replace(",","")
    if len(splitline)==11:
        pos=splitline[2]; pos=pos.replace(",","")
        print splitline[1]+"\t"+pos+"\t"+pos+"\t"+splitline[0]+"\t"+splitline[3]+"\t"+splitline[5]+"\t"+splitline[6]+"\t"+splitline[7]+"\t"+splitline[8]+"\t"+splitline[8]+"\t"+splitline[9]+"\t"+splitline[10]
    elif len(splitline)==13:
        print splitline[1]+"\t"+pos+"\t"+pos+"\t"+splitline[0]+"\t"+splitline[3]+"\t"+splitline[5]+"\t"+splitline[6]+"\t"+splitline[7]+"\t"+splitline[8]+"\t"+splitline[10]+"\t"+splitline[11]+"\t"+splitline[12]
file.close()
