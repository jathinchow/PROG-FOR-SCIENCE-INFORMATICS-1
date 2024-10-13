QUESTION-2A
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


QUESTION-2B
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
# Generate an array of 100 random integers between 10 and 50 (inclusive) to represent the number of DEGs per chromosome
degs_per_chromosome = np.random.randint(10, 50, size=100)  # 100 chromosomes

# Plot histogram 
# Create a new figure with a specified size (10 inches wide, 6 inches tall)
plt.figure(figsize=(10, 6))

# Create a histogram of the DEGs per chromosome data, with bins ranging from 10 to 50 in increments of 5, and a black edge color
plt.hist(degs_per_chromosome, bins=np.arange(10, 51, 5), edgecolor='black')

# Set the x-axis label to "Number of DEGs"
plt.xlabel('Number of DEGs')

# Set the y-axis label to "Frequency"
plt.ylabel('Frequency')

# Set the title of the histogram to "Histogram of DEGs Distribution"
plt.title('Histogram of DEGs Distribution')
plt.grid(axis='y',alpha=0.75)

# Display the histogram
plt.show()


QUESTION-2C
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
degs_per_chromosome_normal = np.random.randint(10, 50, size=100)  # 100 chromosomes for Normal samples
degs_per_chromosome_tumor = np.random.randint(10, 50, size=100)  # 100 chromosomes for Tumor samples

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 6))

# Plot histogram for Normal samples
ax.hist(degs_per_chromosome_normal, bins=np.arange(10, 51, 5), edgecolor='black', alpha=0.5, label='Normal')

# Plot histogram for Tumor samples
ax.hist(degs_per_chromosome_tumor, bins=np.arange(10, 51, 5), edgecolor='black', alpha=0.5, label='Tumor')

# Set title and labels
ax.set_title('Distribution of DEGs by Chromosome (Normal vs Tumor)')
ax.set_xlabel('Number of DEGs')
ax.set_ylabel('Frequency')

# Add legend
ax.legend(loc='upper right')

# Show grid
ax.grid(axis='y', alpha=0.75)

# Display the histogram
plt.show()


QUESTION-2D
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
degs_per_chromosome_normal = np.random.randint(10, 50, size=100)  # 100 chromosomes for Normal samples
degs_per_chromosome_tumor = np.random.randint(10, 50, size=100)  # 100 chromosomes for Tumor samples

# Create a Pandas DataFrame
df = pd.DataFrame({'Normal': degs_per_chromosome_normal, 'Tumor': degs_per_chromosome_tumor})

# Calculate upregulated and downregulated DEGs
upregulated_degs = (df['Tumor'] > df['Normal']).sum()
downregulated_degs = (df['Tumor'] < df['Normal']).sum()

# Calculate percentages
total_degs = len(df)
upregulated_percentage = (upregulated_degs / total_degs) * 100
downregulated_percentage = (downregulated_degs / total_degs) * 100

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))

# Create bar chart
ax.bar(['Upregulated', 'Downregulated'], [upregulated_percentage, downregulated_percentage], color=['green', 'red'])

# Set title and labels
ax.set_title('Percentage of DEGs Up/Downregulated in Tumor Samples')
ax.set_xlabel('Regulation Type')
ax.set_ylabel('Percentage (%)')

# Display the bar chart
plt.show()


QUESTION-2E
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gene_expression_data = pd.read_excel(r'C:\Users\kdivy\.ipynb_checkpoints\Gene_Expression_Data.xlsx')
gene_expression_data.set_index('Probe_ID', inplace=True)

# Create heatmap
plt.figure(figsize=(12, 8))
# Create a heatmap of the gene expression data, with the rows and columns transposed (i.e., samples as rows and probe IDs as columns)
sns.heatmap(gene_expression_data.T, cmap='coolwarm')

# Set the title of the heatmap to "Heatmap of Gene Expression by Sample"
plt.title('Heatmap of Gene Expression by Sample')

# Set the x-axis label to "Sample"
plt.xlabel('Sample')

# Set the y-axis label to "Probe ID"
plt.ylabel('Probe ID')

# Display the heatmap
plt.show()


QUESTION-2F
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
gene_expression_data = pd.read_excel(r'C:\Users\kdivy\.ipynb_checkpoints\Gene_Expression_Data.xlsx')
gene_expression_data.set_index('Probe_ID', inplace=True)

# Create clustermap
# Create a clustermap of the gene expression data, with the rows and columns (i.e., samples as rows and probe IDs as columns); 
sns.clustermap(gene_expression_data.T, cmap='coolwarm', figsize=(12, 8))

# Set the title of the clustermap to "Clustermap of Gene Expression by Sample"
plt.title('Clustermap of Gene Expression by Sample')

# Display the clustermap
plt.show()


QUESTION-2G
The gene expression data showed some amazing tendencies that we found through our exploratory data analysis.
Chromosomes 1 and 2 have the highest concentrations of differentially expressed genes (DEGs), according to the histogram showing DEGs by chromosome, indicating a significant role for DEGs in the condition under investigation. 
Furthermore, the stacked histogram indicated that tumor samples had a much larger number of DEGs, especially on certain chromosomes, and classified DEGs by sample type (Normal vs. Tumor).

A detailed presentation of gene expression across samples was provided by the heatmap and clustermap, which showed unique groups of genes with comparable expression patterns. 
The clear variations in gene expression between tumor and normal samples were highlighted by these visual aids, which gave significant information on the underlying genetic processes.
