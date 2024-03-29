# Copyright 2020 The ASReview Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import OrderedDict
import os

import matplotlib.pyplot as plt
import numpy as np

from asreview.analysis.analysis import Analysis as BaseAnalysis
from matplotlib.colors import to_rgb
from asreview.analysis.statistics import _get_labeled_order


class Analysis(BaseAnalysis):
    def recall_at_limit(self, limit=0, result_format="percentage",
                        final_labels=False):
        if final_labels:
            labels = self.final_labels
        else:
            labels = self.labels

        n_included = np.sum(labels)
        all_n_labeled = []
        for logger in self.loggers.values():
            n_current_included = 0
            n_labeled = 0
            _, n_initial = _get_labeled_order(logger)
            for query_i in range(logger.n_queries()):
                label_idx = logger.get("label_idx", query_i=query_i)
                for idx in label_idx:
                    inclusion = labels[idx]
                    n_current_included += inclusion
                    n_labeled += 1
                    if n_current_included == n_included - limit:
                        all_n_labeled.append(n_labeled)
                        break
                if n_current_included == n_included - limit:
                    break
        if result_format == "percentage":
            mult = 100/(len(labels)-n_initial)
        else:
            mult = 1
        return mult*(np.average(all_n_labeled)-n_initial)


def _add_recall(limit, analysis, ax, col, result_format, text_at=None,
                box_dist=0.5, add_value=False, **kwargs):
    if limit is None:
        return

    text = f"{limit} missing"
    recall = analysis.recall_at_limit(limit, result_format=result_format,
                                      **kwargs)
    if recall is None:
        return

    if add_value:
        text += r"$\approx" + f" {recall:.2f}" + r"\%$"
    if text_at is None:
        text_at = (recall + box_dist, 50)
    plt.plot((recall, recall), (recall, 100), color=col, ls="--")
    plt.plot((recall, recall), (0, recall), color=col, ls=":")
    bbox = dict(boxstyle='round', facecolor=col)
    ax.text(*text_at, text, color="black", bbox=bbox)


def _add_WSS(WSS, analysis, ax, col, result_format, text_at=None,
             box_dist=0.5,
             add_value=False, **kwargs):
    if WSS is None:
        return

    text = f"WSS@{WSS}%"
    WSS_val, WSS_x, WSS_y = analysis.wss(WSS, x_format=result_format, **kwargs)
    if WSS_x is None or WSS_y is None:
        return

    if add_value:
        text += r"$\approx" + f" {round(WSS_val, 2)}" + r"\%$"

    if text_at is None:
        text_at = (WSS_x[0] + box_dist, (WSS_y[0] + WSS_y[1])/2)
    plt.plot(WSS_x, WSS_y, color=col, ls="--")
    plt.plot(WSS_x, (0, WSS_y[0]), color=col, ls=":")
    bbox = dict(boxstyle='round', facecolor=col)
    ax.text(*text_at, text, color="black", bbox=bbox)


def _add_RRF(RRF, analysis, ax, col, result_format, text_at=None, box_dist=0.5,
             add_value=False, **kwargs):
    if RRF is None:
        return

    RRF_val, RRF_x, RRF_y = analysis.rrf(RRF, x_format=result_format, **kwargs)
    if RRF_x is None or RRF_y is None:
        return

    text = f"RRF@{RRF}%"
    if add_value:
        text += r"$\approx" + f" {round(RRF_val, 2)}" + r"\%$"

    RRF_x = 0, RRF_x[0]
    RRF_y = RRF_y[1], RRF_y[1]
    if text_at is None:
        text_at = (RRF_x[0] + box_dist, RRF_y[0] + box_dist + 2)

    plt.plot(RRF_x, RRF_y, color=col, ls="--")
    bbox = dict(boxstyle='round', facecolor=col)
    ax.text(*text_at, text, color="black", bbox=bbox)


def _add_random(text_at, ax, col='black'):
    bbox = dict(boxstyle='round', facecolor='0.65')
    ax.text(*text_at, "random", color="black", bbox=bbox)


class Plot():
    def __init__(self, paths, prefix="result"):
        self.analyses = OrderedDict()
        self.is_file = OrderedDict()

        for path in paths:
            new_analysis = Analysis.from_path(path, prefix=prefix)
            if new_analysis is not None:

                data_key = new_analysis.key
                self.analyses[data_key] = new_analysis
                if os.path.isfile(path):
                    self.is_file[data_key] = True
                else:
                    self.is_file[data_key] = False

    def __enter__(self):
        return self

    def __exit__(self, *_, **__):
        for analysis in self.analyses.values():
            analysis.close()

    @classmethod
    def from_paths(cls, paths, prefix="result"):
        plot_inst = Plot(paths, prefix=prefix)
        return plot_inst

    def plot_time_to_inclusion(self, X_fp):
        for data_key, analysis in self.analyses.items():
            results = analysis.time_to_inclusion(X_fp)
            for key in results["ttd"]:
                plt.plot(results["x_range"], results["ttd"][key],
                         label=data_key + " - " + key)
        plt.legend()
        plt.show()

    def plot_time_to_discovery(self, result_format="percentage"):
        avg_times = []
        for analysis in self.analyses.values():
            results = analysis.avg_time_to_discovery(
                result_format=result_format)
            avg_times.append(list(results.values()))

        if result_format == "number":
            plt.hist(avg_times, 30, histtype='bar', density=False,
                     label=self.analyses.keys())
            plt.xlabel("# Reviewed")
            plt.ylabel("# of papers included")
        else:
            plt.hist(avg_times, 30, histtype='bar', density=True,
                     label=self.analyses.keys())
            plt.xlabel("% Reviewed")
            plt.ylabel("Fraction of papers included")
        plt.legend()
        plt.show()

    def plot_inc_found(self, result_format="percentage", abstract_only=False,
                       legend=True, wss_value=False, rrf_value=False,
                       x_lim=(0, 100), y_lim=(0, 100),
                       rrf_at_list=[], wss_at_list=[], recall_at_list=[],
                       random_at=None):
        """
        Plot the number of queries that turned out to be included
        in the final review.
        """
        legend_name = []
        legend_plt = []

        fig, ax = plt.subplots()

        max_len = 0
        for i, data_key in enumerate(reversed(self.analyses)):
            analysis = self.analyses[data_key]

            inc_found = analysis.inclusions_found(result_format=result_format)
            n_initial = analysis.inc_found[False]["n_initial"]
            n_after_init = len(analysis.labels) - n_initial
            max_len = max(max_len, n_after_init)
            if result_format == "percentage":
                box_dist = 0.5
            else:
                box_dist = 100
            col = "C"+str((len(self.analyses)-1-i) % 10)
            text_col = list(to_rgb(col))
            for _i in range(3):
                text_col[_i] += 0.15
                text_col[_i] = min(1, text_col[_i])
            if (legend or i == len(self.analyses)-1) and not abstract_only:
                print(wss_at_list)
                for wss_at in wss_at_list:
                    _add_WSS(wss_at["value"],
                             analysis, ax, result_format=result_format, col=text_col,
                             text_at=wss_at["text_at"],
                             add_value=wss_value)
                for rrf_at in rrf_at_list:
                    _add_RRF(rrf_at["value"],
                             analysis, ax, result_format=result_format, col=text_col,
                             text_at=rrf_at["text_at"], add_value=rrf_value)
                for recall_at in recall_at_list:
                    _add_recall(
                        recall_at["value"], analysis, ax, col=text_col,
                        result_format=result_format, text_at=recall_at["text_at"],
                        add_value=recall_at.get("add_value", True))

            if random_at is not None:
                _add_random(random_at, ax, col='black')

            if self.is_file[data_key]:
                line_width = 0.7
            else:
                line_width = 2

            myplot = plt.errorbar(*inc_found, color=col, lw=line_width)
            if abstract_only:
                legend_name.append(f"{data_key} (abstract)")
            else:
                legend_name.append(f"{data_key}")
            legend_plt.append(myplot)

            if result_format == "percentage":
                plt.plot(inc_found[0], inc_found[0], color='black', ls="--")

            if abstract_only:
                col = "#ff6666"
                inc_found_final = analysis.inclusions_found(
                    result_format=result_format, final_labels=True)
                for wss_at in wss_at_list:
                    _add_WSS(wss_at["value"],
                             analysis, ax, col, result_format,
                             text_at=wss_at["text_at"],
                             add_value=wss_value,
                             final_labels=True)
                for rrf_at in rrf_at_list:
                    _add_RRF(rrf_at["value"],
                             analysis, ax, col, result_format,
                             text_at=rrf_at["text_at"], add_value=rrf_value,
                             final_labels=True)
                for recall_at in recall_at_list:
                    _add_recall(
                        recall_at["value"], analysis, ax, col=col,
                        result_format=result_format, text_at=recall_at["text_at"],
                        add_value=recall_at.get("add_value", True),
                        final_labels=True)

                col = "red"

                _, WSS95_x, _ = analysis.wss(95, x_format=result_format,
                                             final_labels=True)
                _, WSS100_x, _ = analysis.wss(100, x_format=result_format,
                                              final_labels=True)
                bbox = dict(boxstyle='round', facecolor=col, alpha=0.5)
                prev_value = 0
                x_vals = []
                y_vals = []
                WSS_added = False
                for i in range(len(inc_found_final[0])):
                    if inc_found_final[1][i] != prev_value:
                        x_vals.append(inc_found_final[0][i])
                        y_vals.append(inc_found[1][i])
                        prev_value = inc_found_final[1][i]
                        if inc_found_final[0][i] >= WSS100_x[0] - 1e-4 and not WSS_added:
                            ax.text(WSS100_x[0]+300, inc_found[1][i],
                                    "WSS@100%", color="white", bbox=bbox)
                            WSS_added = True
                myplot = plt.scatter(x_vals, y_vals, color=col)
                legend_name.append(f"{data_key} (final)")
                legend_plt.append(myplot)

        if legend:
            plt.legend(legend_plt, legend_name, loc="lower right")

        if result_format == "number":
            ax2 = ax.twiny()
            ax.set_xlim(0, max_len)
            ax2.set_xlim(0, 100)
            ax.set_xlabel("# Reviewed")
            ax2.set_xlabel("% Reviewed")
            ax.set_ylabel("# Inclusions found")
            symb = "#"
        elif result_format == "percentage":
            symb = "%"
            ax.set_xlabel("% Reviewed")
            ax.set_ylabel("% Inclusions found")
            ax.set_xlim(*x_lim)
            ax.set_ylim(*y_lim)
        else:
            symb = "?"

        plt.grid()
        fig.tight_layout()
        plt.show()

    def plot_limits(self, prob_allow_miss=[0.1, 0.5, 2.0],
                    result_format="percentage"):
        legend_plt = []
        legend_name = []
        linestyles = ['-', '--', '-.', ':']

        for i, data_key in enumerate(self.analyses):
            res = self.analyses[data_key].limits(
                prob_allow_miss=prob_allow_miss,
                result_format=result_format)
            x_range = res["x_range"]
            col = "C"+str(i % 10)

            for i_limit, limit in enumerate(res["limits"]):
                ls = linestyles[i_limit % len(linestyles)]
                my_plot, = plt.plot(x_range, np.array(limit)+np.array(x_range),
                                    color=col, ls=ls)
                if i_limit == 0:
                    legend_plt.append(my_plot)
                    legend_name.append(f"{data_key}")

        plt.plot(x_range, x_range, color="black", ls='--')
        if result_format == "percentage":
            plt.xlabel("% of papers read")
            plt.ylabel("Estimate of % of papers that need to be read")
        else:
            plt.xlabel("# of papers read")
            plt.ylabel("Estimate of # of papers that need to be read")
        plt.legend(legend_plt, legend_name, loc="upper right")
        plt.title("Articles left to read")
        plt.grid()
        plt.show()
