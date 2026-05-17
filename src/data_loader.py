import yfinance as yf
import numpy as np


def fetch_market_data(
    tickers,
    start_date,
    end_date
):

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )['Close']

    data = data.dropna()

    return data


def calculate_log_returns(data):

    log_returns = np.log(
        data / data.shift(1)
    )

    return log_returns.dropna()