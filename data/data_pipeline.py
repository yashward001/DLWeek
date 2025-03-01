# data_pipeline.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def simulate_data(start_date="2022-01-01", periods=1000, freq="H"):
    """
    Simulate historical stock data.

    Parameters:
        start_date (str): Simulation start date.
        periods (int): Number of periods to simulate.
        freq (str): Frequency of data (e.g., "H" for hourly).

    Returns:
        DataFrame: Simulated price data with datetime index.
    """
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    np.random.seed(42)
    prices = np.random.uniform(low=100, high=200, size=len(date_range))
    high = prices + np.random.uniform(0, 5, size=len(date_range))
    low = prices - np.random.uniform(0, 5, size=len(date_range))
    volume = np.random.randint(1000, 5000, size=len(date_range))
    df = pd.DataFrame({
        "close": prices,
        "high": high,
        "low": low,
        "volume": volume
    }, index=date_range)
    return df

def preprocess_data(df):
    """
    Clean and preprocess the data.
    - Sorts the DataFrame by index.
    - Computes the percentage return.

    Returns:
        DataFrame: Preprocessed DataFrame.
    """
    df.sort_index(inplace=True)
    df["return"] = df["close"].pct_change()
    df.dropna(inplace=True)
    return df

def compute_indicators(df):
    """
    Compute a variety of technical indicators and add them to the DataFrame.
    Indicators include:
      - RSI_14
      - MACD, MACD_signal, MACD_hist
      - ROC_14
      - SMA_10, SMA_50
      - Bollinger Bands (BB_Middle, BB_Upper, BB_Lower)
      - ATR_14
      - Rolling Mean and STD (20)
      - Z_Score_20
      - VWAP (intraday)
      - ADX_14, +DI14, -DI14
      - Ichimoku Cloud components (Tenkan_Sen, Kijun_Sen, Senkou_Span_A, Senkou_Span_B)
      - Stochastic Oscillator (%K and %D)

    Returns:
        DataFrame: DataFrame with the new indicator columns.
    """
    # RSI (14)
    def compute_RSI(series, period=14):
        delta = series.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period, min_periods=period).mean()
        avg_loss = loss.rolling(window=period, min_periods=period).mean()
        rs = avg_gain / (avg_loss + 1e-9)
        rsi = 100 - (100 / (1 + rs))
        return rsi

    df["RSI_14"] = compute_RSI(df["close"], period=14)

    # MACD (12,26,9)
    ema12 = df["close"].ewm(span=12, adjust=False).mean()
    ema26 = df["close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema12 - ema26
    df["MACD_signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
    df["MACD_hist"] = df["MACD"] - df["MACD_signal"]

    # ROC (14)
    df["ROC_14"] = df["close"].pct_change(periods=14) * 100

    # Moving Averages: SMA_10 and SMA_50
    df["SMA_10"] = df["close"].rolling(window=10).mean()
    df["SMA_50"] = df["close"].rolling(window=50).mean()

    # Bollinger Bands (20,2)
    df["BB_Middle"] = df["close"].rolling(window=20).mean()
    df["BB_Std"] = df["close"].rolling(window=20).std()
    df["BB_Upper"] = df["BB_Middle"] + 2 * df["BB_Std"]
    df["BB_Lower"] = df["BB_Middle"] - 2 * df["BB_Std"]

    # ATR (14)
    prev_close = df["close"].shift(1)
    tr1 = df["high"] - df["low"]
    tr2 = (df["high"] - prev_close).abs()
    tr3 = (df["low"] - prev_close).abs()
    df["TR"] = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    df["ATR_14"] = df["TR"].rolling(window=14).mean()

    # Rolling Mean and STD (20)
    df["Rolling_Mean_20"] = df["close"].rolling(window=20).mean()
    df["Rolling_STD_20"] = df["close"].rolling(window=20).std()

    # Z Score (20)
    df["Z_Score_20"] = (df["close"] - df["Rolling_Mean_20"]) / df["Rolling_STD_20"]

    # VWAP (Intraday)
    df["Date"] = df.index.date
    df["TPV"] = ((df["high"] + df["low"] + df["close"]) / 3) * df["volume"]
    df["Cumulative_TPV"] = df.groupby("Date")["TPV"].cumsum()
    df["Cumulative_Volume"] = df.groupby("Date")["volume"].cumsum()
    df["VWAP"] = df["Cumulative_TPV"] / df["Cumulative_Volume"]
    df.drop(["Date", "TPV", "Cumulative_TPV", "Cumulative_Volume"], axis=1, inplace=True)

    # ADX (14) with +DI and -DI
    df["UpMove"] = df["high"] - df["high"].shift(1)
    df["DownMove"] = df["low"].shift(1) - df["low"]
    df["+DM"] = np.where((df["UpMove"] > df["DownMove"]) & (df["UpMove"] > 0), df["UpMove"], 0)
    df["-DM"] = np.where((df["DownMove"] > df["UpMove"]) & (df["DownMove"] > 0), df["DownMove"], 0)
    df["+DM14"] = df["+DM"].rolling(window=14).sum()
    df["-DM14"] = df["-DM"].rolling(window=14).sum()
    df["TR14"] = df["TR"].rolling(window=14).sum()
    df["+DI14"] = 100 * (df["+DM14"] / (df["TR14"] + 1e-9))
    df["-DI14"] = 100 * (df["-DM14"] / (df["TR14"] + 1e-9))
    df["DX"] = 100 * (abs(df["+DI14"] - df["-DI14"]) / (df["+DI14"] + df["-DI14"] + 1e-9))
    df["ADX_14"] = df["DX"].rolling(window=14).mean()

    # Ichimoku Cloud Components
    df["Tenkan_Sen"] = (df["high"].rolling(window=9).max() + df["low"].rolling(window=9).min()) / 2
    df["Kijun_Sen"] = (df["high"].rolling(window=26).max() + df["low"].rolling(window=26).min()) / 2
    df["Senkou_Span_A"] = ((df["Tenkan_Sen"] + df["Kijun_Sen"]) / 2).shift(26)
    df["Senkou_Span_B"] = ((df["high"].rolling(window=52).max() + df["low"].rolling(window=52).min()) / 2).shift(26)

    # Stochastic Oscillator (%K and %D, 14/3)
    lowest_low_14 = df["low"].rolling(window=14).min()
    highest_high_14 = df["high"].rolling(window=14).max()
    df["Stoch_%K"] = 100 * ((df["close"] - lowest_low_14) / (highest_high_14 - lowest_low_14 + 1e-9))
    df["Stoch_%D"] = df["Stoch_%K"].rolling(window=3).mean()

    # Clean up temporary columns for ADX Calculation
    df.drop(["UpMove", "DownMove", "+DM", "-DM", "+DM14", "-DM14", "TR14", "DX"], axis=1, inplace=True)
    
    return df

def visualize_data(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["close"], label="Close Price")
    plt.plot(df.index, df["SMA_10"], label="SMA 10")
    plt.plot(df.index, df["SMA_50"], label="SMA 50")
    plt.xlabel("Date/Time")
    plt.ylabel("Price (USD)")
    plt.title("Stock Price and Moving Averages")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def save_final_data(df, filename="final_indicators.csv"):
    df.to_csv(filename)
    print(f"Final data with indicators saved to {filename}")

def run_quantitative_analysis_pipeline():
    """
    Run the full quantitative analysis pipeline:
      1. Data simulation/ingestion
      2. Data cleaning & preprocessing
      3. Technical indicator calculation
      4. (Optional) Visualization
      5. Saving final processed data
    Returns:
        DataFrame: Final DataFrame with computed indicators.
    """
    df_raw = simulate_data(start_date="2022-01-01", periods=1000, freq="H")
    print("Raw data:")
    print(df_raw.head())
    
    df_clean = preprocess_data(df_raw)
    df_indicators = compute_indicators(df_clean)
    print("\nData with Technical Indicators:")
    print(df_indicators.head())
    
    visualize_data(df_indicators)
    save_final_data(df_indicators, filename="final_indicators.csv")
    
    return df_indicators

# If run as a script, execute the pipeline.
if __name__ == "__main__":
    final_df = run_quantitative_analysis_pipeline()
