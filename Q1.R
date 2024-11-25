# gene_expression_analysis.R

# Load necessary libraries
library(openxlsx) # For reading Excel files
library(dplyr)    # For data manipulation
library(tidyr)    # For reshaping data

# Set working directory (adjust path if necessary)
setwd("C:/Users/Public/Downloads")

# Load data
gene_expr_data <- read.xlsx("Gene_Expression_Data.xlsx", sheet = 1)  # Load Excel file
sample_info <- read.delim("Sample_Information.tsv")                  # Load TSV file

# Ensure consistent column naming in sample_info
colnames(sample_info)[colnames(sample_info) == "group"] <- "SampleID"

# Reshape gene expression data to long format and merge with sample information
merged_data <- gene_expr_data %>%
  pivot_longer(
    cols = -Probe_ID,        # Keep Probe_ID column intact
    names_to = "SampleID",   # New column for sample IDs
    values_to = "Expression" # Column for expression values
  ) %>% 
  left_join(sample_info, by = "SampleID") %>%        # Merge phenotype information
  mutate(
    SampleID = paste(SampleID, ifelse(patient == "tumor", "Tumor", "Normal"), sep = "_")
  )

# Reshape back to wide format with updated sample names
updated_gene_expr_data <- merged_data %>% 
  select(Probe_ID, SampleID, Expression) %>% 
  pivot_wider(
    names_from = SampleID,
    values_from = Expression
  )

# View and save the updated gene expression data
cat("\nUpdated Gene Expression Data:\n")
print(head(updated_gene_expr_data))  # Display a preview of the updated data

# Save the updated data to a CSV file
write.csv(updated_gene_expr_data, "Updated_Gene_Expression_Data.csv", row.names = FALSE)
cat("\nUpdated data saved to 'Updated_Gene_Expression_Data.csv'\n")
