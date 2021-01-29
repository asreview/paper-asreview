# Scripts for '*ASReview: Open Source Software for Efficient and Transparent Active Learning for Systematic Reviews*'

This repository contains the scripts of the simulation study found in the paper *ASReview: Open Source Software for Efficient and Transparent Active Learning for Systematic Reviews*. This paper introduces the [ASReview project](https://github.com/asreview) and the [ASReview LAB software](https://github.com/asreview/asreview). The results of the simulation study are available via: [10.17605/OSF.IO/2JKD6](https://www.doi.org/10.17605/OSF.IO/2JKD6).

:raised_hand: The scripts in this repository make use of ASReview version 0.7.2. Many improvements were made to the ASReview software afterward. We encourage you to use the [latest version](https://pypi.org/project/asreview/) for new studies. See the [extensive ASReview documentation](https://asreview.readthedocs.io/en/latest/) for all features of ASReview for screening and simulating. 

:arrows_counterclockwise: A persistent version of the scripts can be found on Zenodo `Ferdinands et al. (2020, September 11). Scripts for 'ASReview: Open Source Software for Efficient and Transparent Active Learning for Systematic Reviews' (Version v1.0.1). Zenodo.` http://doi.org/10.5281/zenodo.4024122.

## Installation

Running this simulation study requires Python 3.6+. The results in this repository are generated with ASReview v0.7.2. To run the code in parallel, you also need an implementation of the MPI standard. The most well known standard is [OpenMPI](https://www.open-mpi.org/) (this is not a python package and should be installed separately).

Install the python depencies with
```
pip install -r requirements.txt
```

## Simulation study

This directory contains scripts to reproduce reproduce the results of simulation study for the paper *ASReview: Open Source Software for Efficient and Transparent Active Learning for Systematic Reviews*. It consists of three parts:

1) [optimizing hyperparameters](Hyperparameter_optimization)
2) [simulating systematic reviews](Simulation)
3) [visualizing the simulation results](Visualization)

The figure in the paper displays the performance of an Automated Systematic Review model (Naive Bayes + TF-IDF + Certainty + Dynamic Supersampling) over 15 runs on four already labeled datasets. See paper for details on the datasets.

The simulation output is available on the [Open Science Framework](https://www.doi.org/10.17605/OSF.IO/2JKD6).

## License

The scripts in this repository are MIT licensed. 

## Contact

Questions or remarks? Please send an email to asreview@uu.nl. 

