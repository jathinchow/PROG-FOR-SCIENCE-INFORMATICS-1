QUESTION-1A
# To load the data in to python
import pandas as pd

# Load Gene Expression Data from Excel file
gene_expression_data = pd.read_excel('Gene_Expression_Data.xlsx')

# Load Gene Information from CSV file
gene_information = pd.read_csv('Gene_Information.csv')

# Load Sample Information from TSV file
sample_information = pd.read_csv('Sample_Information.tsv', sep='\t')


QUESTION-1B
# To change sample names 
# Create a dictionary mapping original sample names to new sample names
sample_name_map = {}
for index, row in sample_information.iterrows():
    sample_name = row.get('Sample_Name')  # Use get method to avoid KeyError
    if sample_name is not None:  # Check if sample_name is not None
        phenotype = row.get('Phenotype')  # Use get method to avoid KeyError
        if sample_name in sample_name_map:
            count = 1
            while f"{sample_name}_{phenotype}_{count}" in sample_name_map.values():
                count += 1
            sample_name_map[sample_name] = f"{sample_name}_{phenotype}_{count}"
        else:
            sample_name_map[sample_name] = f"{sample_name}_{phenotype}"

# Rename the sample names in the Gene Expression Data
gene_expression_data.columns = [sample_name_map.get(col, col) for col in gene_expression_data.columns]
print(gene_expression_data.head())  # Print the first few rows of the dataframe


QUESTION-1C
# Split the merged data into two parts based on their labeled phenotype
tumor_data = gene_expression_data.filter(like='_tumor_')
normal_data = gene_expression_data.filter(like='_normal_')
print("Tumor Data:")
print(tumor_data.head())
print("\nNormal Data:")
print(normal_data.head())

QUESTION-1D
# Compute the average expression for each probe from the 2 data sets
tumor_avg_expression = tumor_data.mean(axis=1)
normal_avg_expression = normal_data.mean(axis=1)
print("Tumor Average Expression:")
print(tumor_avg_expression.head())
print("\nNormal Average Expression:")
print(normal_avg_expression.head())

QUESTION-1E
# Determine the fold change for each probe between the two groups
fold_change = (tumor_avg_expression - normal_avg_expression) / normal_avg_expression
print("Fold Change:")
print(fold_change.head())

QUESTION-1F
merged_data = pd.merge(fold_change_df, gene_info, left_on='Probe', right_on='Probe_ID')
# Identify genes with a fold change magnitude (absolute value) greater than 5
high_fold_change_genes = merged_data[abs(merged_data['Fold Change']) > 5]
print("Genes with fold change magnitude > 5:")
print(high_fold_change_genes.head())

QUESTION-1G
high_fold_change_genes['Expression_Status'] = high_fold_change_genes['Fold Change'].apply(
    lambda x: 'Tumor' if x > 0 else 'Normal'
)
# Print the updated dataframe to check the result
print("Genes with fold change magnitude > 4 and expression status:")
print(high_fold_change_genes.head())
