# Simulation
The configuration file resulting from the hyperparameter optimization (`BCTD.ini`) is manually adjusted for the simulation: the n_instances parameter is updated from `20` to `1`.

Run the following lines one by one in the bash shell to simulate an Automated Systematic Review on the four datasets.

#### Simulate Virus Systematic Review (Figure 4A)
```
asreview simulate-batch data/virus.csv --config_file config/BDTW_simualtion.ini --state_file "output/virus/results.h5" -r 15
```

#### Simulate Hall Systematic Review (Figure 4B)
```
asreview simulate-batch data/hall.csv  --config_file config/BDTW_simualtion.ini --state_file "output/hall/results.h5" -r 15
```
#### Simulate PTSD Systematic Review (Figure 4C)
```
asreview simulate-batch data/ptsd.csv  --config_file config/BDTW_simualtion.ini --state_file "output/ptsd/results.h5" -r 15
```

#### Simulate ACE Systematic Review (Figure 4D)
```
asreview simulate-batch data/ace.csv  --config_file config/BDTW_simualtion.ini --state_file "output/ace/results.h5" -r 15
```
