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
# an empty dictionary to store the sample name mappings
sample_name_map = {}
# Iterate over each row in the sample information DataFrame
for index, row in sample_information.iterrows():
    # Get the sample name from the current row, using the get method to avoid a KeyError if the column doesn't exist 
    sample_name = row.get('Sample_Name') 
    if sample_name is not None:  # Check if sample_name is not None
         # Get the phenotype from the current row, using the get method to avoid a KeyError if the column doesn't exist
        phenotype = row.get('Phenotype')  # Use get method to avoid KeyError
         # Check if the sample name is already in the dictionary
        if sample_name in sample_name_map:
            # Initialize a count variable to 1
            count = 1
             # Check if the new sample name (with count) is already in the dictionary values
            while f"{sample_name}_{phenotype}_{count}" in sample_name_map.values():
                count += 1
            # Add the new sample name (with count) to the dictionary
            sample_name_map[sample_name] = f"{sample_name}_{phenotype}_{count}"
        else:
            # Add the new sample name (without count) to the dictionary
            sample_name_map[sample_name] = f"{sample_name}_{phenotype}"
# Rename the sample names in the Gene Expression Data
# The get method is used to retrieve the new sample name from the dictionary, or the original column name if it's not in the dictionary
gene_expression_data.columns = [sample_name_map.get(col, col) for col in gene_expression_data.columns]
print(gene_expression_data.head())  # Print the first few rows of the dataframe


QUESTION-1C
# Split the merged data into two parts based on their labeled phenotype
# This will create a new DataFrame, tumor_data, that contains only the tumor samples
tumor_data = gene_expression_data.filter(like='_tumor_')
# Filter the gene expression data to include only columns that contain the string '_normal_' in their name
# This will create a new DataFrame, normal_data, that contains only the normal samples
normal_data = gene_expression_data.filter(like='_normal_')
print("Tumor Data:")
# The head() method is used to display the first few rows of the DataFrame
print(tumor_data.head())
# Print the first few rows of the normal_data DataFrame to verify the filtering
# The head() method is used to display the first few rows of the DataFrame
print("\nNormal Data:")
print(normal_data.head())


QUESTION-1D
# Compute the average expression for each probe from the 2 data sets
# Calculate the mean of each row in the tumor_data DataFrame, which represents the average expression value for each probe
# The axis=1 parameter specifies that the mean should be calculated along the rows
tumor_avg_expression = tumor_data.mean(axis=1)
# Calculate the mean of each row in the normal_data DataFrame, which represents the average expression value for each probe
# The axis=1 parameter specifies that the mean should be calculated along the rows
normal_avg_expression = normal_data.mean(axis=1)
print("Tumor Average Expression:")
print(tumor_avg_expression.head())
print("\nNormal Average Expression:")
print(normal_avg_expression.head())


QUESTION-1E
# Determine the fold change for each probe between the two groups
# Calculate the fold change for each probe by dividing the difference in average expression between the tumor and normal groups
# Calculate the fold change for each probe using the formula: (tumor_avg - normal_avg) / normal_avg
fold_change = (tumor_avg_expression - normal_avg_expression) / normal_avg_expression
print("Fold Change:")
print(fold_change.head())


QUESTION-1F
# Convert the fold_change Series to a DataFrame with a named column
# The to_frame() method is used to convert the Series to a DataFrame, and the column is named 'Fold Change'
fold_change_df = fold_change.to_frame('Fold Change')
# Reset the index of the DataFrame
fold_change_df.reset_index(inplace=True)
# Rename the index column to 'Probe_ID'
fold_change_df.rename(columns={'index': 'Probe_ID'}, inplace=True)  
# Convert 'Probe_ID' column to a common data type
fold_change_df['Probe_ID'] = fold_change_df['Probe_ID'].astype(str)
gene_information['Probe_ID'] = gene_information['Probe_ID'].astype(str)
# Merge the fold_change_df and gene_information DataFrames based on the 'Probe_ID' column
merged_data = pd.merge(fold_change_df, gene_information, left_on='Probe_ID', right_on='Probe_ID')
# The resulting DataFrame, high_fold_change_genes, contains the genes with a fold change magnitude greater than 5
high_fold_change_genes = merged_data[abs(merged_data['Fold Change']) > 5]


QUESTION-1G
# Filter rows where the absolute value of 'Fold Change' is greater than 5
high_fold_change_genes = merged_data[abs(merged_data['Fold Change']) > 5]
# Add a new column to indicate whether the gene is higher expressed in "Normal" or "Tumor"
# If the fold change is positive, the gene is higher expressed in "Tumor"
# If the fold change is negative, the gene is higher expressed in "Normal"
high_fold_change_genes['Expression_Status'] = high_fold_change_genes['Fold Change'].apply(
    lambda x: 'Tumor' if x > 0 else 'Normal'
)
# Print the result to check the first few rows
print("Genes with fold change magnitude > 5 and expression status:")
print(high_fold_change_genes.head())
