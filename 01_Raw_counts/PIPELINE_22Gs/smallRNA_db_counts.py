#usage python smallRNA_db_counts.py db_file.fa collapsed_reads_file.fa
#header must be in the format ">length,firstnt,numreads" (output of fasta_len_nt_collapsed.py)"

import sys
mirbase_file=open(sys.argv[1],"r")
id_hash={}

for line in mirbase_file:
    if line.startswith(">"):
        line=line.replace(">","")
        id=line.rstrip("\n")
    else:
        seq=line.rstrip("\n")
        id_hash[seq]=id
mirbase_file.close()


fastacol_file=open(sys.argv[2],"r")

for line in fastacol_file:
    if line.startswith(">"):
        id=line.rstrip("\n")
    else:
        seq=line.rstrip("\n")
        if seq in id_hash:
            counts=id.split(",")[2]
            print id_hash[seq]+"\t"+seq+"\t"+counts
fastacol_file.close()
