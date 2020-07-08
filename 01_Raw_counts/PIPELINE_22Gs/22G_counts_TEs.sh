#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -l select=1:ncpus=24:mem=10gb

module load anaconda2/personal

cd /rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/epiMALs_JAN2019/gen_by_gen_experiment/small_rna_seq/fastq/22Gs

htseq-count --stranded=reverse -f bam -r pos $file ../../../../../EpiMALs/VK_MALs/RNA-seq/annotations/c_elegans.PRJNA13758.WS252.annotations.transposons_longest_withgeneatt.gtf > $file.TEcounts

