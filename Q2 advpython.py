#To perform exploratory data analysis on the genes from part 1g
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
gene_expression_data = pd.read_excel(r'C:\Users\kdivy\.ipynb_checkpoints\Gene_Expression_Data.xlsx')

# Check the data shape and info
print(gene_expression_data.shape)
print(gene_expression_data.info())

# Check for missing values
print(gene_expression_data.isnull().sum())

# Convert relevant columns to numeric, if necessary
# Assuming the first column is gene names and the rest are expression values
gene_expression_data.iloc[:, 1:] = gene_expression_data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Visualize the distribution of gene expression values for the first numeric column
plt.figure(figsize=(10, 6))
sns.histplot(gene_expression_data.iloc[:, 1], kde=False)  # Change index if needed
plt.title('Distribution of Gene Expression Values')
plt.xlabel('Gene Expression Value')
plt.ylabel('Frequency')
plt.show()

# Visualize the correlation between genes
corr_matrix = gene_expression_data.iloc[:, 1:].corr()  # Exclude gene names
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation between Genes')
plt.xlabel('Genes')
plt.ylabel('Genes')
plt.show()

# Identify the top 10 most highly expressed genes
top_10_genes = gene_expression_data.iloc[:, 1:].mean().sort_values(ascending=False).head(10)  # Exclude gene names
print(top_10_genes)

# Visualize the expression levels of the top 10 genes
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_genes.index, y=top_10_genes.values)
plt.title('Expression Levels of Top 10 Genes')
plt.xlabel('Gene')
plt.ylabel('Expression Level')
plt.show()
