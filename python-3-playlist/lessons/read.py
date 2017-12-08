ipsum_file = open("files/ipsum.txt")

#for loop method
for line in ipsum_file:
    print(line.rstrip())

#readlines method w/ seek
ipsum_file.seek(0)
lines = ipsum_file.readlines()
print(lines)

#read a specific amount of characters in file
ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)
ipsum_file.close()

#with method
#personal note: looks similar to how the using statement in C# works
def sequence_filter(line):
    return '>' not in line

with open("files/dna_sequence.txt") as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))