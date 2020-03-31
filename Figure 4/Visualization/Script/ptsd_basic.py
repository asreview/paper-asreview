#!/usr/bin/env python

import os
from plot import Plot

data_dir = "simoutput/ptsd"
data_files = os.listdir(data_dir)
data_files = [os.path.join(data_dir, data_file) for data_file in data_files]

with Plot.from_paths([data_dir, *data_files]) as plot:
    rrf_at_list = [{"value": 10, "text_at": (0.5, 70)}]
    wss_at_list = [{"value": 95, "text_at": (5, 80)},
                   {"value": 100, "text_at": (10, 90)}]
    plot.plot_inc_found(legend=False, wss_value=True, rrf_value=True,
                        x_lim=(0, 101),
                        y_lim=(0, 101),
                        rrf_at_list=rrf_at_list,
                        wss_at_list=wss_at_list,
                        random_at=(35, 50),
                        )
