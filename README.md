# From the DNA
**Start here**: [`hiv.py`](hiv.py)
## ️📜Background
This is a small hack of mine I put together to learn more about reverse engineering the DNA and implementation of the central dogma of molecular bio in code.

## ⚒️Progress
[`utils.py`](utils.py) is a custom module containing useful functions written from scratch.


`transcription`  function converts DNA to mRNA. `rna_translation` function converts mRNA sequence to a chain of [amino acids](https://en.wikipedia.org/wiki/Amino_acid) which also can be viewed in short-form or full-length-forms using `translation_shortform` and `translation_fullform` functions respectively.

Proteins are being stored in a FASTA file (check [`proteins.fasta`](/sequence-data/proteins.fasta) for example) for all orders of ORFS's (first, second and third) in both forward and reverse chains.

[`dna_features_viewer`](https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer) module is being used to visualise the DNA. Check example [here](/sequence-data/sequence.png)

[`visualize.py`](visualise.py) uses [ESM1B](https://github.com/facebookresearch/esm#quickstart) (an LLM for proteins) to convert amino acid sequences into PDB format and then uses [ProDy](http://prody.csb.pitt.edu/) & [Matplotlib](https://matplotlib.org/) to 3d visualise the protein strand.

Note : only the largest protein strand of each ORF is being plotted while the length of protein strand also being under 400 due to ESM1B API constraint.

[`3dmol.ipynb`](3dmol.ipynb) uses [py3Dmol](https://pypi.org/project/py3Dmol/) to individually visualise better model of all the ORFs (dna + rna, all orders)

## 📌Examples
[`hiv.py`](hiv.py) contains an implementation of all the functions over the genome of sequence of HIV-1. The accuracy is quite decent so far, majority of proteins have been verified from the [official site](https://www.ncbi.nlm.nih.gov/nuccore/AF033819)