import sys
epis=open(sys.argv[1],"r")
episet=set()
for line in epis:
    episet.add(line.rstrip("\n"))
epis.close()

mRNA_gff=open(sys.argv[2],"r")
for line in mRNA_gff:
    line=line.rstrip("\n")
    splitline=line.split("\t")
    info=splitline[8]
    if splitline[2]=="gene":
        gene_name=info.split(";")[3]
        gene_name=gene_name.split("=")[1]

        if gene_name in episet:
            print line+"\t"+gene_name

mRNA_gff.close()
