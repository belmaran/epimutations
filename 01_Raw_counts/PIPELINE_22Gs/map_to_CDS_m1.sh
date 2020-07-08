#!/bin/sh                                                                      
#PBS -l walltime=24:00:00                                                    
#PBS -l select=1:ncpus=24:mem=10gb

#wrapper shell script for small RNA mapping of uncollapsed libraries to C. elegans CDS


cd /rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/epiMALs_JAN2019/gen_by_gen_experiment/small_rna_seq/fastq/

module load anaconda2/personal
module load bowtie/0.12.7
module load samtools/1.3.1
module load bedtools/2.25.0


file=${file%.fasta};
echo $file;

python /work/ab6415/scripts/filter_22Gs_fasta.py $file.fasta > $file.22Gs.fasta

bowtie /rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/EpiMALs/VK_MALs/RNA-seq/index/all_transcripts_longest \
-f $file.22Gs.fasta -v 0 -S -p 16 -m 1 > $file.maptoCDS.sam
samtools view -bS $file.maptoCDS.sam > $file.maptoCDS.bam
bedtools bamtobed -i $file.maptoCDS.bam > $file.maptoCDS.bed
rm $file.maptoCDS.sam

python /work/ab6415/scripts/collapse_bed.py $file.maptoCDS.bed \
> $file.maptoCDS.col.bed

sort $file.maptoCDS.col.bed > $file.maptoCDS.col.sorted.bed
rm $file.maptoCDS.sorted.bed
rm $file.maptoCDS.col.bed
mv $file.maptoCDS.col.sorted.bed $file.maptoCDS.col.bed

bowtie /rds/general/user/ab6415/projects/lms-sarkies-analysis/live/Toni/EpiMALs/VK_MALs/RNA-seq/index/cel_genomeWS252_bowtie1 \
-f $file.22Gs.fasta -v 0 -S -p 16 -m 1 > $file.maptogenome.sam
samtools view -bS $file.maptogenome.sam > $file.maptogenome.bam
rm $file.maptogenome.sam
samtools sort -o $file.maptogenome.sorted.bam $file.maptogenome.bam
rm $file.maptogenome.bam
samtools index $file.maptogenome.sorted.bam
