Information:
Name of Programmer: Divya Reddy Konda 
Date:October 12th,2024

Overview:
This project aims to analyze gene expression data to identify differentially expressed genes (DEGs) between tumor and normal samples. By integrating multiple data sources, we seek to gain insights into the biological implications of gene expression patterns in cancer.

Prerequisites:
Python 3.x
Libraries: pandas, numpy, matplotlib, seaborn, openpyxl
Datasets:
Gene_Expression_Data.xlsx
Gene_Information.csv
Sample_Information.tsv

Dataset Description:
Gene_Expression_Data.xlsx: Contains gene expression values for various samples.
Gene_Information.csv: Provides information about the genes, including their IDs and descriptions.
Sample_Information.tsv: Lists sample IDs along with their corresponding phenotypes (tumor or normal).

Steps Performed:
Data Loading: All datasets were imported into Python using pandas.
Sample Name Modification: Sample names in the gene expression data were updated based on the phenotypes from the sample information file.
Data Splitting: The merged dataset was divided into two groups based on phenotype (tumor and normal).
Identification of Significant Genes: Genes with an absolute fold change greater than 5 were identified, along with their expression direction.
Exploratory Data Analysis (EDA): Various visualizations were created to explore the data, including histograms of DEGs by chromosome and a heatmap of gene expression across samples.

Visualizations:
Heatmap: Displays gene expression levels across samples, revealing clusters of genes with similar expression patterns.
Histograms: Show the distribution of DEGs by chromosome and segregated by sample type (normal vs. tumor).
Bar Chart: Illustrates the proportions of DEGs that are upregulated versus downregulated in tumor samples.
Clustermap: Provides a hierarchical clustering representation of gene expression data.

Findings:
The analysis revealed considerable differences in gene expression between tumor and normal samples, with a significant number of genes showing upregulation in tumors. Chromosomal analysis identified specific regions with a higher density of differentially expressed genes (DEGs), which could be crucial for comprehending tumor biology.



