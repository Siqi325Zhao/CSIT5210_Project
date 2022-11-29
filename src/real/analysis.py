# some analysis and visualization functions
from pathlib import Path
from pandas import DataFrame
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize():
    plt.style.use('ggplot')

    registered_colors = {
        "Max": "tab:red",
        "Exposure-Based": "tab:blue",
        "NSW": "tab:purple",
        "0-NSW": "tab:purple",
        "1-NSW": "tab:orange",
        "0.5-NSW": "tab:brown",
        "2-NSW": "tab:green",
        "Uniform": "tab:gray",
    }

    metric_list = ["mean_max_envy", "pct_better_off", "pct_worse_off", "user_util"]
    title_dict = {
        "mean_max_envy": "(a) Mean Max Envy",
        "pct_better_off": "(b) % Items Better Off",
        "pct_worse_off": "(c) % Items Worse Off",
        "user_util": "(d) User Utility",
    }

    df = pd.read_csv("./varying_K/result_df.csv")
    legend = ["Max", "Exposure-Based", "Uniform", "1-NSW", "NSW"]
    palette = [registered_colors[l] for l in legend]

    df = pd.read_csv("./varying_K/result_df.csv")
    fig, ax = plt.subplots(1, 4, figsize=(45, 10), tight_layout=True)
    for i, metric in enumerate(metric_list):
        ax_ = ax[i]
        sns.lineplot(
            marker="o",
            markersize=15,
            markers=True,
            linewidth=8,
            ax=ax_,
            x="K",
            y=metric,
            hue="policy",
            legend=False,
            palette=palette,
            data=df,
        )
        # title
        ax_.set_title(title_dict[metric], fontsize=52)
        # yaxis
        ax_.set_ylabel("")
        if metric == "pct_better_off":
            ax_.set_ylim(15, 105)
            ax_.set_yticks([20, 40, 60, 80, 100])
        elif metric == "pct_worse_off":
            ax_.set_ylim(-4, 85)
            ax_.set_yticks([0, 20, 40, 60, 80])
        elif metric == "mean_max_envy":
            ax_.set_ylim(-0.005, 0.125)
            ax_.set_yticks([0.0, 0.04, 0.08, 0.12])
        ax_.tick_params(axis="y", labelsize=35)
        ax_.yaxis.set_label_coords(-0.1, 0.5)
        # xaxis
        ax_.set_xticks([1, 3, 5, 10, 20])
        ax_.set_xlabel(r"Length of Ranking ($K$)", fontsize=44)
        ax_.tick_params(axis="x", labelsize=40)
        ax_.xaxis.set_label_coords(0.5, -0.125)
    fig.legend(
        legend, fontsize=50, 
        bbox_to_anchor=(0.5, 1.12),
        ncol=4, loc="center",
    )