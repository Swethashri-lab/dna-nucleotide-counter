# DNA Nucleotide Counter
# My first bioinformatics project

def count_nucleotides(dna):
    count_A = dna.count("A")
    count_T = dna.count("T")
    count_G = dna.count("G")
    count_C = dna.count("C")
    
    print("DNA Sequence:", dna)
    print("Length:", len(dna))
    print("A count:", count_A)
    print("T count:", count_T)
    print("G count:", count_G)
    print("C count:", count_C)

my_sequence = "ATGCATGCTTAAGCCTTAGC"
count_nucleotides(my_sequence)
