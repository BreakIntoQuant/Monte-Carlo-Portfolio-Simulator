import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_simulation_paths(
    simulations
):

    plt.figure(figsize=(14, 7))

    plt.plot(
        simulations[:, :250],
        alpha=0.08
    )

    plt.title(
        'Monte Carlo Portfolio Simulations'
    )

    plt.xlabel('Trading Days')

    plt.ylabel('Portfolio Value')

    plt.grid(True)

    plt.savefig(
        'charts/monte_carlo_paths.png'
    )

    print(
        "Simulation paths saved."
    )


def plot_terminal_distribution(
    simulations
):

    terminal_values = (
        simulations[-1, :]
    )

    plt.figure(figsize=(12, 6))

    sns.histplot(
        terminal_values,
        bins=60,
        kde=True
    )

    plt.title(
        'Terminal Portfolio Value Distribution'
    )

    plt.xlabel('Portfolio Value')

    plt.ylabel('Frequency')

    plt.grid(True)

    plt.savefig(
        'charts/terminal_distribution.png'
    )

    print(
        "Distribution chart saved."
    )


def plot_confidence_bands(
    simulations,
    lower_band,
    median_band,
    upper_band
):

    days = np.arange(
        len(lower_band)
    )

    plt.figure(figsize=(14, 7))

    plt.fill_between(
        days,
        lower_band,
        upper_band,
        alpha=0.3,
        label='90% Confidence Interval'
    )

    plt.plot(
        days,
        median_band,
        linewidth=2,
        label='Median Simulation'
    )

    plt.title(
        'Monte Carlo Confidence Bands'
    )

    plt.xlabel('Trading Days')

    plt.ylabel('Portfolio Value')

    plt.legend()

    plt.grid(True)

    plt.savefig(
        'charts/confidence_bands.png'
    )

    print(
        "Confidence band chart saved."
    )