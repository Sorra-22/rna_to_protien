import sys

def rn_to_protein(rna_seq):
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    protein = []

    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i + 3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == "Stop":
                break
            protein.append(amino_acid)
    return "".join(protein)

def get_fasta(file_path):
    try:
        with open(file_path, 'r') as file:
            rna_seq = []
            for line in file:
                line = line.strip("\n")

                if not line.startswith(">"):
                    rna_seq.append(line)

            return "".join(rna_seq)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def main():
    rna_seq = get_fasta("sequence.fasta")
    protein = rn_to_protein(rna_seq)
    print(protein)
    print(len(protein))

if __name__ == "__main__":
    main()



