# From the DNA
**Start here**: [`hiv.py`](/hiv-1/hiv)
## ️📜Background
This is a small hack of mine I put together to learn more about reverse engineering the DNA and implementation of the central dogma of molecular bio in code.

## ⚒️Progress
[`utils.py`](utils.py) is a custom module containing useful functions written from scratch.


`transcription`  function converts DNA to mRNA. `rna_translation` function converts mRNA sequence to a chain of [amino acids](https://en.wikipedia.org/wiki/Amino_acid) which also can be viewed in short-form or full-length-forms using `translation_shortform` and `translation_fullform` functions respectively.

Proteins are being stored in a FASTA file (check [`proteins.fasta`](/hiv-1/proteins.fasta) for example) for all orders of ORFS's (first, second and third) in both forward and reverse chains.

[`dna_features_viewer`](https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer) module is being used to visualise the DNA.

## 📌Examples
[`hiv-1`](/hiv-1) contains an implementation of all the functions over the genome of sequence of HIV-1. The accuracy is quite decent so far, majority of proteins have been verified from the [official site](https://www.ncbi.nlm.nih.gov/nuccore/AF033819)
