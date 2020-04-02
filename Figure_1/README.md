# Number of publications
This directory contains scripts to reproduce the results of Figure 1 for the paper ' ASReview: Open Source Software for Efficient and Transparent Systematic Reviews'. It consists of three parts: 1) getting the data, 2) processing the data for visualization, 3) visualizing the data.

Figure 1 displays the number of new COVID-19 publications per week from Nov 14, 2019 until March 15, 2020, as well as the cumulative number over this time period. 

The information is based on the CORD-19 dataset made available through a collaboration of the Allen Institute for AI, the Chan Zuckerberg Initiative, Georgetown University’s Center for Security and Emerging Technology, Microsoft Research, and the National Library of Medicine of the National Institutes of Health. Version 4 of the dataset (updated March 20, 2020) contains metadata of 44K publications on COVID-19 and coronavirus-related research (e.g. SARS, MERS, etc.) from PubMed Central, the WHO COVID-19 database of publications,  the preprint servers bioRxiv and medRxiv and papers contributed by specific publishers

Information on publication time in the original dataset is enriched with information from Crossref (for DOIs) and EuropePMC (for PMCIDs). The enriched dataset has date information on date of publication in standard format for 97% of all records. 



# Languages
Scripts for part 1 (getting data) are written in R. 
Scrips for part 2 and 3 (preprocessing and visualization) are written in Python. 

# Install packages
For part 1 (getting data), the following R packages are required

```
install.packages("tidyverse")
install.packages("lubridate")
install.packages("rcrossref")
install.packages("europepmc")
```

For part 3 (visualizing data), the following python packages are required

```
pip install pandas
pip install numpy
pip install matplotlib.pyplot
```