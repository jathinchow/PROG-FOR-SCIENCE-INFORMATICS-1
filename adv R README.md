## Information:
Name of Programmer: Divya Reddy Konda ;
Language: R ;
Version: version 4.4.2 ;
Date: 24th November,2024 ;

## Required Software:
R (version 4.0 or higher recommended): Download and install from CRAN.
RStudio (optional, but recommended): Provides an integrated development environment for running and editing R scripts.

## Data Files
- Gene_Expression_Data.xlsx: Contains gene expression data.
- Gene_Information.csv: Contains gene information.
- Sample_Information.tsv: Contains sample information with phenotypes.

## Steps
1. Load the data files into R.
2. Change sample names based on phenotype.
3. Merge data and split based on phenotype.
4. Compute average expression for all genes.
5. Determine log2 fold change for each probe.
6. Identify genes with fold change magnitude > 5.
7. Add column for higher expression in Normal or Tumor samples.
8. Perform exploratory data analysis (EDA).
9. Create visualizations (histograms, bar chart, heatmap, clustermap).

## Findings
1. The histogram presents the distribution of DEGs by chromosome, with some chromosomes having higher concentrations of DEGs.
2. The stacked histogram depicts DEGs by chromosome, further distinguished into upregulated or downregulated genes.
3. In the pie chart, there is an overview of the percentage of genes upregulated in tumor versus normal samples.
4. The heatmap illustrates gene expression levels across tumor and normal samples.
5. The clustermap groups the top 100 genes with the highest log2 fold change to show patterns of similarity in expression.
These analyses inform on differential expression both at gene and sample levels.


