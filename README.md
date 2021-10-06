# Helper scripts to organise ASV data generated from Gallus gallus microbiota

## Introduction

This repository contains several Python scripts that were used to organise Amplicon Sequencing Variant (ASV) datasets generated from 16S sequencing data of *Gallus gallus* reproductive and digestive tracts (male and female), as generated by Dr. Liisa Veerus.

There are three scripts:

1. `GenerateSeparateAndCombinedASVs.py`: Takes in ASVs from various datasets and records in which datasets is each ASV found. Also constructs a file with the union of all ASVs found.
2. `GenerateTypeCountsAndPhylaGeneraCounts.py`: Takes in a table of each ASV and its corresponding phylum and genus and generates a new table of the different ASVs found for each phylum and genus observed.
3. `UnioniseFemaleAndMales.py`: Takes in files corresponding to male-specific and female-specific ASVs for each sample and generates a count matrix with the samples as rows and ASV IDs as columns.

## Requirements

Only `UnioniseFemaleAndMales.py` requires an additional Python library, pandas. Please see the installation instructions [here](https://pandas.pydata.org/getting_started.html) to install pandas.

## Running scripts

All scripts can be run using, e.g.:

```python GenerateSeparateAndCombinedASVs.py```

or, if one is using Python 3:

```python3 GenerateSeparateAndCombinedASVs.py```

Each script contains references to data that has not been uploaded with this repository. To make full use of the script, please replace the data directories, input file names, and output file names appropriately.
