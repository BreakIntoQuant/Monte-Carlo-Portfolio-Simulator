import numpy as np


def monte_carlo_simulation(
    prices,
    log_returns,
    weights,
    num_simulations=10000,
    trading_days=252
):

    mean_returns = (
        log_returns.mean() * 252
    )

    covariance_matrix = (
        log_returns.cov() * 252
    )

    portfolio_mean = np.sum(
        mean_returns * weights
    )

    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(
                covariance_matrix,
                weights
            )
        )
    )

    dt = 1 / trading_days

    initial_portfolio_value = 100000

    simulations = np.zeros(
        (trading_days, num_simulations)
    )

    for sim in range(num_simulations):

        portfolio_path = [
            initial_portfolio_value
        ]

        for day in range(trading_days):

            random_shock = np.random.normal()

            drift = (
                portfolio_mean
                - 0.5
                * portfolio_volatility**2
            ) * dt

            diffusion = (
                portfolio_volatility
                * np.sqrt(dt)
                * random_shock
            )

            next_value = (
                portfolio_path[-1]
                * np.exp(
                    drift + diffusion
                )
            )

            portfolio_path.append(
                next_value
            )

        simulations[:, sim] = (
            portfolio_path[1:]
        )

    return simulations