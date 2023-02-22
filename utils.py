# GC content
def gc_content(string):
    G = string.count("G")
    C = string.count("C")
    percentage = ((G+C)/int(len(string))) * 100

    return percentage

# DNA to mRNA conversion
def transcription(dna):
    dna = dna.upper()
    compliment = ""
    for i in dna:
        if i == "A":
            compliment += "T"
        elif i == "T":
            compliment += "A"
        elif i == "G":
            compliment += "C"
        elif i == "C":
            compliment += "G"

    return compliment.replace("T", "U")

# Breaking DNA/mRNA strings into ORF list
# Order describes type of ORF — first, second or third
# Direction specifies forward chain or reverse chain
def orf(string, order, direction):
    str_reverse = string[::-1]
    if order == "first" and direction == "forward":
        return [string[i:i+3] for i in range(0, len(string), 3)]

    if order == "second" and direction == "forward":
        return [string[i:i+3] for i in range(1, len(string), 3)]

    if order == "third" and direction == "forward":
        return [string[i:i+3] for i in range(2, len(string), 3)]

    if order == "first" and direction == "reverse":
        return [str_reverse[i:i+3] for i in range(0, len(str_reverse), 3)]

    if order == "second" and direction == "reverse":
        return [str_reverse[i:i+3] for i in range(1, len(str_reverse), 3)]

    if order == "third" and direction == "reverse":
        return [str_reverse[i:i+3] for i in range(2, len(str_reverse), 3)]

# Converting mRNA to proteins
def rna_translation(rna):

    if type(rna) == list:

        temp = ""
        rna_str = ""

        for i in rna:
            rna_str += i

        rna_codon = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                     "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                     "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                     "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                     "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                     "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                     "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                     "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                     "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                     "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                     "UAA": "_", "CAA": "Q", "AAA": "K", "GAA": "E",
                     "UAG": "_", "CAG": "Q", "AAG": "K", "GAG": "E",
                     "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                     "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                     "UGA": "_", "CGA": "R", "AGA": "R", "GGA": "G",
                     "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                     }

        if len(rna_str) % 3 == 0:
            for i in range(0, len(rna)):
                temp += rna_codon[rna[i]]

            return temp
        else:
            for i in range(0, len(rna)-1):
                temp += rna_codon[rna[i]]

            return temp

# Converting DNA to proteins
def dna_translation(dna):

    if type(dna) == list:

        temp = ""
        dna_str = ""

        for i in dna:
            dna_str += i

        dna_codon = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
                     'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
                     'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
                     'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
                     'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
                     'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
                     'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
                     'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
                     'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
                     'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                     'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
                     'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
                     'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
                     'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
                     'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
                     'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
                     }

        if len(dna_str) % 3 == 0:
            for i in range(0, len(dna)):
                temp += dna_codon[dna[i]]

            return temp
        else:
            for i in range(0, len(dna)-1):
                temp += dna_codon[dna[i]]

            return temp

# Converting protein strand to full-form amino acids
def translation_shortform(string):

    temp = ""
    amino_acid = {'C': 'CYS',
                  'D': 'ASP',
                  'S': 'SER',
                  'Q': 'GLN',
                  'K': 'LYS',
                  'I': 'ILE',
                  'P': 'PRO',
                  'T': 'THR',
                  'F': 'PHE',
                  'N': 'ASN',
                  'G': 'GLY',
                  'H': 'HIS',
                  'L': 'LEU',
                  'R': 'ARG',
                  'W': 'TRP',
                  'A': 'ALA',
                  'V': 'VAL',
                  'E': 'GLU',
                  'Y': 'TYR',
                  'M': 'MET',
                  "_": "_"}

    for i in string:
        temp += (amino_acid[i] + " ")

    return temp

# Converting short-form protein strand to full-form amino acids
def translation_fullform(string):
    i = string.split()
    temp = ""
    acids = {
        "ALA": "ALANINE",
        "ASX": "ASPARTIC ACID OR ASPARAGINE",
        "CYS": "CYSTEINE",
        "ASP": "ASPARTIC ACID",
        "GLU": "GLUTAMIC ACID",
        "PHE": "PHENYLALANINE",
        "GLY": "GLYCINE",
        "HIS": "HISTIDINE",
        "ILE": "ISOLEUCINE",
        "LYS": "LYSINE",
        "LEU": "LEUCINE",
        "MET": "METHIONINE",
        "ASN": "ASPARAGINE",
        "PRO": "PROLINE",
        "GLN": "GLUTAMINE",
        "ARG": "ARGININE",
        "SER": "SERINE",
        "THR": "THREONINE",
        "USEC": "SELENOCYSTEINE",
        "VAL": "VALINE",
        "TRP": "TRYPTOPHAN",
        "TYR": "TYROSINE",
        "GLX": "GLUTAMIC ACID",
        "_": "_"

    }

    for e in i:
        temp += (acids[e] + " ")

    return temp
