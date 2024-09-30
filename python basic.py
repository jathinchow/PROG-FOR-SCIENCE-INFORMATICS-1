## Question-1
# Open the sequence file in read mode
with open('chr1_GL383518v1_alt.fa', 'r') as file:
# Read all lines from the file into a list
    lines = file.readlines()
# Initialize an empty string to store the sequence
sequence = ""
# Concatenate all lines of the sequence, skipping the header
for line in lines[1:]:
    sequence += line.strip()
# Print the 10th letter of the sequence (index 9 because of zero-based indexing)
print("10th letter of the sequence:", sequence[9])
# Print the 758th letter of the sequence (index 757 because of zero-based indexing)
print("758th letter of the sequence:", sequence[757])


## Question-2
# open the sequence file and read its content
with open("chr1_GL383518v1_alt.fa", "r") as file:
# Read the entire file, remove newline characters, convert to uppercase, and skip the first character
    sequence = file.read().replace("\n", "").upper()[1:]  
# Create the reverse complement of the DNA sequence
# Translate ACGT to TGCA and then reverse the string
rev_comp = sequence.translate(str.maketrans('ACGT', 'TGCA'))[::-1]
# Print the 79th letter of the reverse complement (index 78 because of zero-based indexing)
print("79th letter of reverse complement:", rev_comp[78])
# Print the letters from the 500th to the 800th of the reverse complement (slicing from index 499 to 798)
print("500th through 800th letters of reverse complement:", rev_comp[499:799])


## Question-3
# To count nucleotide occurences in kilobase intervals
def count_nucleotides_by_kilobase(sequence, kilobase_size=1000):
# Initialize a dictionary to hold nucleotide counts for each kilobase
    nucleotide_counts = {}
# Iterate over the sequence in steps of kilobase_size
    for i in range(0, len(sequence), kilobase_size):
# Extract the current kilobase segment from the sequence
        kb_segment = sequence[i:i + kilobase_size]
# Count the occurrences of each nucleotide in the kilobase segment
        counts = {
            'A': kb_segment.count('A'),  
            'C': kb_segment.count('C'),  
            'G': kb_segment.count('G'), 
            'T': kb_segment.count('T')  
        }
# Store the counts in the dictionary with the starting index of the kilobase as the key
        nucleotide_counts[i] = counts
# Return the dictionary containing nucleotide counts for each kilobase
    return nucleotide_counts
# Call the function to count nucleotides in the sequence
nucleotide_counts = count_nucleotides_by_kilobase(sequence)
# Iterate over each kilobase starting index and print the nucleotide counts
for kb_start in range(0, len(sequence), 1000):
# Use the get method to retrieve counts safely, defaulting to an empty dictionary if not found
    print(f"Nucleotide counts in kilobase starting at {kb_start}: {nucleotide_counts.get(kb_start, {})}")


## Question 4
# To read dictionary from part 3
nucleotide_counts = count_nucleotides_by_kilobase(sequence)
# To create a list with 4 elements for the first 1000 base pairs
first_kb_counts = nucleotide_counts[0][1]  # Get the counts directly from the tuple
print("Nucleotide counts in the first 1000 base pairs:", first_kb_counts)
# To repeat for each kilobase and create a list of lists
all_kb_counts = []
# Iterate over the sequence in steps of 1000 bases
for kb_start, counts in nucleotide_counts:
# Append the counts to the list of all kilobase counts
    all_kb_counts.append(counts)
# Calculate the sum of nucleotide counts for each kilobase
sums = [sum(kb) for kb in all_kb_counts]
print("Sums of nucleotide counts for each kilobase:", sums)
# To identify kilobases with sums not equal to the expected value
differences = [i for i, s in enumerate(sums) if s != expected_sum]
print("Kilobases with sums not equal to", expected_sum, ":", differences)
# To check if there are any discrepancies
if differences:
    print("The differences are likely due to the fact that the sequence is not perfectly divided into kilobases.")
    print("Some kilobases may have fewer than 1000 base pairs, resulting in a sum less than", expected_sum)
else:
    print("All kilobases have sums equal to", expected_sum)


