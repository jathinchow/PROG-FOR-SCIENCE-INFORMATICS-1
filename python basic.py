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
