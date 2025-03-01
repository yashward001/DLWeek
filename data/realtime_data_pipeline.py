# realtime_data_pipeline.py
import requests
import pandas as pd
import numpy as np
from datetime import datetime

def fetch_alpha_vantage_data(api_key, symbol, function="TIME_SERIES_INTRADAY", interval="60min", outputsize="full"):
    """
    Fetch intraday stock data from Alpha Vantage.
    
    Parameters:
        api_key (str): Your Alpha Vantage API key.
        symbol (str): Stock ticker symbol.
        function (str): API function; default is "TIME_SERIES_INTRADAY".
        interval (str): Data interval; for 1-hour data, use "60min".
        outputsize (str): "full" for all data, "compact" for the latest 100 data points.
    
    Returns:
        DataFrame: Stock data with a datetime index.
    """
    url = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "apikey": api_key,
        "outputsize": outputsize,
        "datatype": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # For intraday data, the key is formatted like "Time Series (60min)"
    ts_key = f"Time Series ({interval})"
    if ts_key not in data:
        raise ValueError("Error retrieving data from Alpha Vantage:", data)
    
    df = pd.DataFrame.from_dict(data[ts_key], orient='index')
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": int})
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    return df

def preprocess_stock_data(df):
    """
    Preprocess the stock DataFrame:
      - Calculate percentage return.
      - Drop missing values.
    """
    df["return"] = df["close"].pct_change()
    df.dropna(inplace=True)
    return df

def compute_technical_indicators(df):
    """
    Compute technical indicators and add them as columns to the DataFrame.
    
    Here we compute:
      - SMA_10 (10-period Simple Moving Average)
      - RSI_14 (14-period Relative Strength Index)
      
    Returns:
        DataFrame: DataFrame with additional indicator columns.
    """
    # SMA_10
    df["SMA_10"] = df["close"].rolling(window=10).mean()
    
    # RSI_14
    def compute_RSI(series, period=14):
        delta = series.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period, min_periods=period).mean()
        avg_loss = loss.rolling(window=period, min_periods=period).mean()
        rs = avg_gain / (avg_loss + 1e-9)
        return 100 - (100 / (1 + rs))
    
    df["RSI_14"] = compute_RSI(df["close"], period=14)
    # (Add more indicators as needed)
    return df

def run_realtime_data_pipeline(api_key, symbol):
    """
    Run the complete real-time data pipeline:
      1. Fetch intraday (1hr) data from Alpha Vantage.
      2. Preprocess the data.
      3. Compute technical indicators.
    
    Returns:
        DataFrame: Processed DataFrame with computed indicators.
    """
    df_raw = fetch_alpha_vantage_data(api_key, symbol, function="TIME_SERIES_INTRADAY", interval="60min", outputsize="full")
    df_clean = preprocess_stock_data(df_raw)
    df_indicators = compute_technical_indicators(df_clean)
    return df_indicators

if __name__ == "__main__":
    # Example usage:
    api_key = "W5LXPX0X4CVPIHLX"  # Replace with your actual API key
    symbol = "AAPL"
    df = run_realtime_data_pipeline(api_key, symbol)
    print("Processed Data:")
    print(df.tail())
