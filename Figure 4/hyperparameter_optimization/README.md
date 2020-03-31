# Hyperparameter optimization
Optimize hyperparameters for 12 hours, over 6 datasets in the `data` directory for a model with Naive Bayes classifier (B), tfidf feature extraction (T), certainty sampling (max) query strategy (C), double balance strategy (D):

`mpirun -n 2 asreview hyper-active -m nb -b double -e tfidf -q max -t 12:00:00 --mpi`

See the [asreview-hyperopt repository](https://github.com/asreview/asreview-hyperopt) for more information on the optimization of hyperparameters.

After 12 hours of optimizing, a configuration file with optimized hyperparameters is created:

`asreview create-config output/active/nb_max_double_tfidf/nudging_software_wilson_ace_virus/trials.pkl -o config/BCTD.ini`
