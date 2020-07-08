#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -l select=1:ncpus=16:mem=100gb

module load bowtie2/2.1.0
module load tophat/2.0.11
module load samtools/0.1.11
module load anaconda2/personal


tophat -i 30 -I 20000 -p 16 -o $file.mapping /rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/EpiMALs/VK_MALs/RNA-seq/index/cel_genomeWS252 \
$file

htseq-count --stranded=reverse -f bam -r pos -t intron \
$file.mapping/accepted_hits.bam \
/rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/epiMALs_JAN2019/gen_by_gen_experiment/RNA_seq/gtf/c_elegans.PRJNA13758.WS252.annotations.mRNA_longest_withgeneatt.gtf \
> $file.intronic.counts

htseq-count --stranded=reverse -f bam -r pos -t exon \
$file.mapping/accepted_hits.bam \
/rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/epiMALs_JAN2019/gen_by_gen_experiment/RNA_seq/gtf/c_elegans.PRJNA13758.WS252.annotations.mRNA_longest_withgeneatt.gtf \
> $file.exon.counts


#htseq-count --help
#Written by Simon Anders (sanders@fs.tum.de), European Molecular Biology
#Laboratory (EMBL). (c) 2010. Released under the terms of the GNU General
#Public License v3. Part of the 'HTSeq' framework, version 0.9.1