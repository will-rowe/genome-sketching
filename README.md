# Genome Sketching

> NOTE: still under development....

## About

This repository accompanies my review of sketching algorithms for genomic data:

> [When The Levee Breaks: a practical guide to sketching algorithms for processing the flood of genomic data]()

The notebooks correspond to the sections in the paper:

* Sketching algorithms
    -   [3.1 Set similarity with MinHash](./notebooks/r3.1.Set-similarity-with-MinHash.ipynb)
    -   [3.2 Set membership with Bloom filter](./notebooks/r3.2.Set-membership-with-Bloom-filters.ipynb)
    -   [3.3 Element frequency with Count-Min sketch](./notebooks/r3.3.Element-frequency-with-Count-Min-sketch.ipynb)
    -   [3.4 Set cardinality with HyperLogLog](./notebooks/r3.4.Set-cardinality-with-HyperLogLog.ipynb)
* Example workflows
    -   [4.1 Overview](./notebooks/r4.1.Workflows-for-genomics.ipynb)
    -   [4.2 Quality check samples](r4.2.Sample-QC.ipynb)
    -   [4.3 AMR gene profiling](r4.3.Resistome-profiling.ipynb)
    -   [4.4 Phylogenetic trees](r4.4.Phylogeny.ipynb)
    -   [4.5 Data mining](r4.5.Data-mining.ipynb)

I've also included a notebook to cover some basic concepts (e.g. *k-mer decomposition*). This notebook is called [Background](./notebooks/Background.ipynb) and we save ourselves some time later by importing the functions from this notebook into the other notebooks (e.g. for reading sequence data files).

If you've not used a Jupyter notebook before, just hit "shift + enter" to run a cell. [Here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) is a good guide to get you started with Jupyter.


## Running the workbooks

To run the workbooks interactively from your browser, use Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/will-rowe/genome-sketching/master?filepath=notebooks)


## Running the workbooks locally

If you want to run the workbooks locally, you'll need `conda` and `jupyter`.

Once you have these, follow these steps:

1. clone the repo
```
git clone https://github.com/will-rowe/genome-sketching

cd genome-sketching
```

2. create the environment
```
conda env create --file=binder/environment.yml

source activate genome-sketching
```

3. run the notebook server
```
jupyter notebook --notebook-dir=./notebooks
```

## See also

As well as the notebooks, this repository also contains a [curated list of bioinformatics tools that use sketching](./references.md). Please let me know if tools need adding, or file a pull request!

## Notes

I'd like to thank Titus Brown and Luiz Irber, who not only got me onto Binder, but also inspired me to review the current sketching methods for genomics (thanks to their excellent [sourmash](https://github.com/dib-lab/sourmash) documentation and examples of MinHash for genomics).