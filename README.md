# Scripts for '*ASReview: Open Source Software for Efficient and Transparent Active Learning for Systematic Reviews*'

This repository contains the scripts of the simulation study found in the paper *ASReview: Open Source Software for Efficient and Transparent Active Learning for Systematic Reviews*. This paper introduces the [ASReview project](https://github.com/asreview) and the [ASReview LAB software](https://github.com/asreview/asreview). The results of the simulation study are available via: [10.17605/OSF.IO/2JKD6](https://www.doi.org/10.17605/OSF.IO/2JKD6).

## Installation

Running this simulation study requires Python 3.6+. The results in this repository have been generated with ASReview v0.7.2. To run the code in parallel, you also need an implementation of the MPI standard. The most well known standard is [OpenMPI](https://www.open-mpi.org/) (this is not a python package and should be installed separately). The details for running the scripts with this older version of ASReview are available on [Zenodo](https://zenodo.org/record/4024122).

It is recommended to use a newer version of ASReview. The new python dependencies can be installed by:
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

Questions or remarks? Please see the [contact page](https://github.com/asreview/asreview#contact). 

