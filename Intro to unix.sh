# Create a directory titled "Informatics_573" 
mkdir Informatics_573 
# To navigate the created directory 
cd Infornatics_573
# To download all secondary assemblies for human chromosome 1 from UCSC Genome browser
wget -r -np -nd -A 'chr1_*' https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/
# Unzip all of the downloaded chromosome 1 assemblies
gunzip chr1_*
# To create a new empty file called "data_summary.txt"
touch data_summary.txt
# To append list of detailed information to "data_summary.txt"
ls -lh >> data_summary.txt
#Append the first 10 lines of each of the chromosome 1 assemblies to “data_summary.txt”
head -n 10 chr1_* >> data_summary.txt
#Append the name of assembly as well as the total number of lines included in that assembly to “data_summary.txt”
wc chr1_* >> data_summary.txt


