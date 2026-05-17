import numpy as np


def calculate_value_at_risk(
    simulations,
    confidence_level=5
):

    terminal_values = (
        simulations[-1, :]
    )

    var = np.percentile(
        terminal_values,
        confidence_level
    )

    return var


def calculate_expected_shortfall(
    simulations,
    confidence_level=5
):

    terminal_values = (
        simulations[-1, :]
    )

    var_threshold = np.percentile(
        terminal_values,
        confidence_level
    )

    shortfall_values = (
        terminal_values[
            terminal_values
            <= var_threshold
        ]
    )

    expected_shortfall = (
        shortfall_values.mean()
    )

    return expected_shortfall


def calculate_probability_of_loss(
    simulations,
    initial_value=100000
):

    terminal_values = (
        simulations[-1, :]
    )

    probability = np.mean(
        terminal_values
        < initial_value
    )

    return probability


def calculate_confidence_intervals(
    simulations
):

    lower_band = np.percentile(
        simulations,
        5,
        axis=1
    )

    median_band = np.percentile(
        simulations,
        50,
        axis=1
    )

    upper_band = np.percentile(
        simulations,
        95,
        axis=1
    )

    return (
        lower_band,
        median_band,
        upper_band
    )