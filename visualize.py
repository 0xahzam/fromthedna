from Bio import SeqIO
from prody import *
from numpy import *
from matplotlib.pyplot import *

# Reading proteins from the FASTA file
temp = list()
with open("sequence-data/proteins.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        temp.append([record.seq])

# DNA ORFs (Open Reading Frames)
dna_orf_1 = str(temp[0][0])
dna_orf_2 = str(temp[1][0])
dna_orf_3 = str(temp[2][0])
neg_dna_orf_1 = str(temp[3][0])
neg_dna_orf_2 = str(temp[4][0])
neg_dna_orf_3 = str(temp[5][0])

# RNA ORFs (Open Reading Frames)
rna_orf_1 = str(temp[6][0])
rna_orf_2 = str(temp[7][0])
rna_orf_3 = str(temp[8][0])
neg_rna_orf_1 = str(temp[9][0])
neg_rna_orf_2 = str(temp[10][0])
neg_rna_orf_3 = str(temp[10][0])

# Finding largest protein strands in each ORF under lenght<400
def maximise(e):
    e = list(filter(lambda x: len(x) < 400, e.split("_")))
    count = 0
    for i in range(0, len(e)):
        if len(e[i]) > count:
            count = len(e[i])

    for i in e:
        if len(i) == count:
            return (i)


biglist = [maximise(dna_orf_1), maximise(dna_orf_2), maximise(dna_orf_3), maximise(neg_dna_orf_1), maximise(neg_dna_orf_2), maximise(neg_dna_orf_3),
           maximise(rna_orf_1), maximise(rna_orf_2), maximise(rna_orf_3), maximise(neg_rna_orf_1), maximise(neg_rna_orf_2), maximise(neg_rna_orf_3)]

# Using ESM1B to convert amino acid sequence to pdb
def esm1b(protein, filename):
    import requests

    url = "https://api.esmatlas.com/foldSequence/v1/pdb/"
    res = requests.post(url, protein)

    with open("sequence-data/{}".format(filename), "w") as f:
        f.write(res.text)

# Plotting DNA Forward ORFs using matplotlib and ProDy
def plot_dna_forward_orfs():
    esm1b(biglist[0], "dna-forward/dna_orf_1.pdb")
    esm1b(biglist[1], "dna-forward/dna_orf_2.pdb")
    esm1b(biglist[2], "dna-forward/dna_orf_3.pdb")

    graph1 = parsePDB('sequence-data/dna-forward/dna_orf_1.pdb')
    graph2 = parsePDB('sequence-data/dna-forward/dna_orf_2.pdb')
    graph3 = parsePDB('sequence-data/dna-forward/dna_orf_3.pdb')

    print(graph1)
    print(graph2)
    print(graph3)

    showProtein(graph1)
    showProtein(graph2)
    showProtein(graph3)
    title("DNA Forward ORFs")
    legend()
    show()

# Plotting DNA Reverse ORFs using matplotlib and ProDy
def plot_dna_reverse_orfs():
    esm1b(biglist[0], "dna-reverse/neg_dna_orf_1.pdb")
    esm1b(biglist[1], "dna-reverse/neg_dna_orf_2.pdb")
    esm1b(biglist[2], "dna-reverse/neg_dna_orf_3.pdb")

    graph1 = parsePDB('sequence-data/dna-reverse/neg_dna_orf_1.pdb')
    graph2 = parsePDB('sequence-data/dna-reverse/neg_dna_orf_2.pdb')
    graph3 = parsePDB('sequence-data/dna-reverse/neg_dna_orf_3.pdb')

    print(graph1)
    print(graph2)
    print(graph3)

    showProtein(graph1)
    showProtein(graph2)
    showProtein(graph3)
    title("DNA Reverse ORFs")
    legend()
    show()

# Plotting RNA Forward ORFs using matplotlib and ProDy
def plot_rna_forward_orfs():
    esm1b(biglist[0], "rna-forward/rna_orf_1.pdb")
    esm1b(biglist[1], "rna-forward/rna_orf_2.pdb")
    esm1b(biglist[2], "rna-forward/rna_orf_3.pdb")

    graph1 = parsePDB('sequence-data/rna-forward/rna_orf_1.pdb')
    graph2 = parsePDB('sequence-data/rna-forward/rna_orf_2.pdb')
    graph3 = parsePDB('sequence-data/rna-forward/rna_orf_3.pdb')

    print(graph1)
    print(graph2)
    print(graph3)

    showProtein(graph1)
    showProtein(graph2)
    showProtein(graph3)
    title("RNA Forward ORFs")
    legend()
    show()

# Plotting DNA Reverse ORFs using matplotlib and ProDy
def plot_rna_reverse_orfs():
    esm1b(biglist[0], "rna-reverse/neg_rna_orf_1.pdb")
    esm1b(biglist[1], "rna-reverse/neg_rna_orf_2.pdb")
    esm1b(biglist[2], "rna-reverse/neg_rna_orf_3.pdb")

    graph1 = parsePDB('sequence-data/rna-reverse/neg_rna_orf_1.pdb')
    graph2 = parsePDB('sequence-data/rna-reverse/neg_rna_orf_2.pdb')
    graph3 = parsePDB('sequence-data/rna-reverse/neg_rna_orf_3.pdb')

    print(graph1)
    print(graph2)
    print(graph3)

    showProtein(graph1)
    showProtein(graph2)
    showProtein(graph3)
    title("RNA Reverse ORFs")
    legend()
    show()

# Uncomment to plot

# plot_dna_forward_orfs()
# plot_dna_reverse_orfs()
# plot_rna_forward_orfs()
# plot_rna_reverse_orfs()