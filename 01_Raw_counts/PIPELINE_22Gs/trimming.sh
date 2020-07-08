#!/bin/sh

module load anaconda2/personal
module load bowtie/0.12.1
module load samtools/1.2
module load bedtools/2.25.0
module load cutadapt/1.10

cutadapt -a TGGAATTCTCGGGTGCCAAGGAA -m 15 -o $FILE.trimmed $FILE
python /work/ab6415/scripts/fastq_2_FASTA_reformatheaders.py $FILE.trimmed > $FILE.format.fasta


