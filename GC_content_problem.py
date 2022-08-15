# Bioinformatics Assignment
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the
# GC-content of that string. Rosalind allows for a default error of 0.001 in all
# decimal answers unless otherwise stated; please see the note on absolute error below.


# Import os and sys
# Navigate to current working directory (cwd)
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

# Open file, split on new fasta file names, '<'
fasta_file_names = []
myText = []
with open('fasta_files.txt', 'r') as f:
    myText = f.read().split('\n')

# May replace 'fasta_files.txt' with any .txt file containing multiple fasta sequences.  See attached example.

start_position= []

# Generate list of fasta file names
for line in myText:
    if line.startswith('>'):
        fasta_file_names.append(line)
        start_position.append(myText.index(line)+1)

print(fasta_file_names)
print(start_position)

# Use start positions of list to generate string for each fasta file
sequences_list = []
# print (len(start_position))
for x in range(0, len(start_position)):
    # print ("x = ", x)
    sequence_string = ''
    if x == (len(start_position)-1):
        for y in range(start_position[x], len(myText)):
            sequence_string = sequence_string + myText[y]
    elif x < (len(start_position)-1):
        for y in range(start_position[x], (start_position[x+1]-1)):
            sequence_string = sequence_string + myText[y]
    # print(sequence_string)
    sequences_list.append(sequence_string)

print (sequences_list)

# Now we have list of fasta file names, and fasta file sequences.
# We can generate new list of GC content.
# Then take max and report fasta file name and GC content.

# GC content list
GCcontent = []
for x in sequences_list:
    gc_count = 0
    for nucleotide in x:
        if nucleotide == 'G' or nucleotide == 'C':
            gc_count += 1
    GCcontent.append(round(float(100 * (gc_count / len(x))), 4))

print (GCcontent)

# Now, figure out which one is highest and report it!
print ('Highest GC content:')
print (fasta_file_names[GCcontent.index(max(GCcontent))])
print (max(GCcontent))
