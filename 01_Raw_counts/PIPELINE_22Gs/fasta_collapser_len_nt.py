#collapses fasta file
#info in the headers: >length,first_nt,nreads

import sys

file = open(sys.argv[1],"r")


sequences={}
for line in file:
	if not line.startswith(">"):
		if line in sequences:
			sequences[line]	= sequences[line]+1
		else:
			sequences[line] = 1

outfile=open(sys.argv[1]+"_len_nt_collapsed","w")

for seq in sequences:
	outfile.write(">"+str(len(seq.rstrip("\n")))+","+seq[0]+","+str(sequences[seq])+"\n")
	outfile.write(seq)

file.close()
outfile.close()

