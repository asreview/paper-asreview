# Simulation study
This directory contains scripts to reproduce reproduce the results of Figure 4 for the paper ' ASReview: Open Source Software for Efficient and Transparent Systematic Reviews'. It consists of three parts: 1) optimizing hyperparameters, 2) simulating systematic reviews, 3) visualizing the simulation results.

Figure 4 displays the performance of an Automated Systematic Review model (Naive Bayes + TF-IDF + Certainty + Dynamic Supersampling) over 15 runs on four already labeled datasets: (A) the virus dataset, (B) the hall dataset, (C) PTSD dataset, (4) ACE dataset.

The simulation output is available on the [Open Science Framework](https://osf.io/2jkd6/).


# Install packages
Make sure you've installed ASReview v0.7.2, the ASReview simulations package and the ASReview visualization package.

```
pip install asreview
pip install asreview-simulation
pip install asreview-visualization
```
