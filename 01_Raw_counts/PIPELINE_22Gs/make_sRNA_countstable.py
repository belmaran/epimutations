#Run as:
#mapped_sRNA_makeTable.py collapsed_bedfile length firstnt strand > outfile

import sys

file=open(sys.argv[1],"r")

target_lengths=sys.argv[2].split(",")
target_firstnt=sys.argv[3]
target_strand=sys.argv[4]

#process bed file and store info in dict
counts_dict={}

for line in file:
    line=line.split("\t")

    gene=line[0]

    srna=line[3]
    srna=srna.split(",")
    length=srna[0]
    firstnt=srna[1]
    count=int(srna[2])
    seq=srna[3]
    strand=line[5].rstrip("\n")

    if length in target_lengths and firstnt==target_firstnt and target_strand==strand:
        if gene in counts_dict:
            counts_dict[gene]=counts_dict[gene]+count
        else:
            counts_dict[gene]=count

file.close()

#write table

for gene in counts_dict:
    print gene+"\t"+str(counts_dict[gene])


