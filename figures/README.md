# paper-asreview-introduction
Scripts to reproduce the results Figure 4 for the paper ' ASReview: Open Source Software for Efficient and Transparent Systematic Reviews'.

See also the output avaialble at OSF: https://osf.io/2jkd6/  DOI 10.17605/OSF.IO/2JKD6

# Simulation

run the following lines one by one in the bash shell to simulate an Automated Systematic Review on the four dataset

#### Figure 4A
```
mpirun -n 2 asreview batch data/virus.csv --config_file BCTW_all.ini --state_file "simoutput/virus/results.h5" -r 15 --server_job
```

#### Figure 4B
```
mpirun -n 2 asreview batch data/hall.csv --config_file BCTW_all.ini --state_file "simoutput/hall/results.h5" -r 15 --server_job
```
#### Figure 4C
```
mpirun -n 2 asreview batch data/ptsd.csv --config_file BCTW_all.ini --state_file "simoutput/ptsd/results.h5" -r 15 --server_job
```

#### Figure 4D
```
mpirun -n 2 asreview batch data/ace.csv --config_file BCTW_all.ini --state_file "simoutput/ace/results.h5" -r 15 --server_job
```

# Visualization
