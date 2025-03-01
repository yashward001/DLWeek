# visualisation.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_price_and_moving_averages(df, close_col="close", sma_cols=["SMA_10", "SMA_50"], title="Stock Price and Moving Averages"):
    """
    Plot the close price along with moving averages.
    
    Parameters:
        df (DataFrame): DataFrame containing price data and moving averages.
        close_col (str): Column name for the close price.
        sma_cols (list): List of column names for simple moving averages.
        title (str): Plot title.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df[close_col], label="Close Price", color="blue")
    for sma in sma_cols:
        plt.plot(df.index, df[sma], label=sma)
    plt.xlabel("Date/Time")
    plt.ylabel("Price (USD)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_balance_history(balance_history, title="Trading Performance - Balance History"):
    """
    Plot the trading account balance history.
    
    Parameters:
        balance_history (list or np.array): A sequence of account balances over time.
        title (str): Plot title.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(balance_history, marker="o", linestyle="-", color="green")
    plt.xlabel("Time Steps")
    plt.ylabel("Account Balance")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_technical_indicator(df, indicator, title=None):
    """
    Plot a specific technical indicator over time.
    
    Parameters:
        df (DataFrame): DataFrame with time-indexed data.
        indicator (str): Column name of the indicator to plot.
        title (str): Plot title; if None, a default title is used.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df[indicator], label=indicator, color="magenta")
    plt.xlabel("Date/Time")
    plt.ylabel(indicator)
    if title is None:
        title = f"{indicator} Over Time"
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_ensemble_performance(balance_history, returns=None, title="Ensemble Trading Performance"):
    """
    Plot both the account balance history and returns from an ensemble simulation.
    
    Parameters:
        balance_history (list or np.array): History of account balances over time.
        returns (list or np.array, optional): History of returns.
        title (str): Overall title for the plots.
    """
    plt.figure(figsize=(12, 10))
    
    # Plot balance history
    plt.subplot(2, 1, 1)
    plt.plot(balance_history, marker="o", color="blue", label="Balance")
    plt.xlabel("Time Steps")
    plt.ylabel("Account Balance")
    plt.title(title + " - Balance History")
    plt.legend()
    plt.grid(True)
    
    # Plot returns if provided
    if returns is not None:
        plt.subplot(2, 1, 2)
        plt.plot(returns, marker="x", color="red", label="Returns")
        plt.xlabel("Time Steps")
        plt.ylabel("Returns")
        plt.title(title + " - Returns")
        plt.legend()
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()
