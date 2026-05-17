from data_loader import (
    fetch_market_data,
    calculate_log_returns
)

from simulation import (
    monte_carlo_simulation
)

from risk_analysis import (
    calculate_value_at_risk,
    calculate_expected_shortfall,
    calculate_probability_of_loss,
    calculate_confidence_intervals
)

from visualization import (
    plot_simulation_paths,
    plot_terminal_distribution,
    plot_confidence_bands
)

import numpy as np


def main():

    tickers = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN"
    ]

    weights = np.array([
        0.25,
        0.25,
        0.25,
        0.25
    ])

    print(
        "\nDownloading market data..."
    )

    prices = fetch_market_data(
        tickers,
        "2020-01-01",
        "2025-01-01"
    )

    print(
        "Calculating log returns..."
    )

    log_returns = (
        calculate_log_returns(
            prices
        )
    )

    print(
        "Running Monte Carlo simulations..."
    )

    simulations = (
        monte_carlo_simulation(
            prices,
            log_returns,
            weights
        )
    )

    print(
        "\nPerforming risk analysis..."
    )

    var = calculate_value_at_risk(
        simulations
    )

    expected_shortfall = (
        calculate_expected_shortfall(
            simulations
        )
    )

    probability_of_loss = (
        calculate_probability_of_loss(
            simulations
        )
    )

    (
        lower_band,
        median_band,
        upper_band
    ) = calculate_confidence_intervals(
        simulations
    )

    print("\n==========")
    print("RISK METRICS")
    print("==========")

    print(
        f"\nValue at Risk (5%): ${var:,.2f}"
    )

    print(
        f"\nExpected Shortfall: ${expected_shortfall:,.2f}"
    )

    print(
        f"\nProbability of Loss: {probability_of_loss:.2%}"
    )

    print(
        "\nGenerating visualizations..."
    )

    plot_simulation_paths(
        simulations
    )

    plot_terminal_distribution(
        simulations
    )

    plot_confidence_bands(
        simulations,
        lower_band,
        median_band,
        upper_band
    )

    print(
        "\nMonte Carlo Portfolio Risk Analysis Complete."
    )


if __name__ == "__main__":
    main()