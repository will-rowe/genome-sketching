<div align="center">
  <h1>Genome Sketching</h1>
  <h3>a review of sketching algorithms for genomic data</h3>
  <hr>
  <a href="https://travis-ci.org/will-rowe/genome-sketching"><img src="https://travis-ci.org/will-rowe/genome-sketching.svg?branch=master" alt="travis"></a>
  <a href="https://zenodo.org/badge/latestdoi/180174530"><img src="https://zenodo.org/badge/180174530.svg" alt="DOI"></a>
  <a href="https://mybinder.org/v2/gh/will-rowe/genome-sketching/master?filepath=notebooks"><img src="https://mybinder.org/badge_logo.svg" alt="binder"></a>
</div>

***

## Overview

This repository accompanies my review of sketching algorithms for genomic data:

> [When The Levee Breaks: a practical guide to sketching algorithms for processing the flood of genomic data](paper/genome-sketching-review.pdf)

The notebooks correspond to the sections in the paper:

* Section 3: Sketching algorithms
    -   [3.1 Set similarity with MinHash](./notebooks/r3.1.Set-similarity-with-MinHash.ipynb)
    -   [3.2 Set membership with Bloom filter](./notebooks/r3.2.Set-membership-with-Bloom-filters.ipynb)
* Section 4: Example workflows for genomics
    -   [Overview](./notebooks/r4.0.Workflows-for-genomics.ipynb)
    -   [Workflow 1: Sample QC](./notebooks/r4.1.Sample-QC.ipynb)
    -   [Workflow 2: Resistome profiling](./notebooks/r4.2.Resistome-profiling.ipynb)
    -   [Workflow 3: Outbreak surveillance](./notebooks/r4.3.Outbreak-surveillance.ipynb)
    -   [Workflow 4: Data mining](./notebooks/r4.4.Data-mining.ipynb)

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

Thanks to [Francesco Mosconi](https://github.com/ghego/travis_anaconda_jupyter) for showing how to use Travis CI for build testing the notebooks.