# StraddleAI

**Team: Innovators Inc.**

## Overview

StraddleAI is a state-of-the-art quantitative trading system that combines real-time stock data, advanced technical indicators, sentiment analysis, reinforcement learning, and a transformer-based meta-model to generate robust trading signals. By fusing diverse data sources and analytical methods, StraddleAI delivers buy, sell, or hold decisions designed to optimize trading performance while managing risk effectively.

---

## Key Features

- **Real-Time Data Integration:**  
  Fetches real-time 1-hour intraday data from Alpha Vantage and preprocesses it to compute essential technical indicators.

- **Advanced Technical Analysis:**  
  Computes a wide range of indicators such as SMA, RSI, MACD, Bollinger Bands, ATR, VWAP, ADX, Ichimoku Cloud components, and Stochastic Oscillators, providing a deep insight into market dynamics.

- **Sentiment Analysis:**  
  Utilizes the Perplexity API and FinBERT to analyze market sentiment based on recent financial news, enhancing the decision-making process.

- **Reinforcement Learning Trading Agent:**  
  Trains a DQN model using historical data to learn optimal trading strategies, enabling dynamic decision-making.

- **Transformer Meta-Model:**  
  Implements a transformer that processes a 29-dimensional input (comprising 14 strategy signals, 14 profitability metrics, and 1 sentiment score) to produce a refined trading signal.

- **Ensemble Decision-Making:**  
  Combines the outputs of the RL agent, traditional technical strategies, and the transformer meta-model into a single final decision (Buy, Sell, or Hold).

- **Risk Management:**  
  Features an integrated risk management module that adjusts position sizes, sets stop-loss and take-profit levels, monitors drawdowns, and ensures robust performance under varying market conditions.

- **Visualization Tools:**  
  Provides comprehensive visualizations including price charts with technical indicators, portfolio balance history, drawdown charts, and more to facilitate performance analysis.

---

## Directory Structure

```plaintext
StraddleAI/
├── main.py                       # Main entry point of the project
├── requirements.txt              # Project dependencies
├── README                        # This readme file
├── data/
│   ├── data_pipeline.py          # (Optional) Simulated data pipeline
│   ├── realtime_data_pipeline.py # Real-time data fetching and preprocessing module
├── models/
│   ├── __init__.py               # Model package initializer
│   ├── rl_model.py               # RL model training/loading module
│   ├── transformer_model.py      # Transformer meta-model and helper functions
│   ├── trained_rl_model_final.zip # Pre-trained RL model file
├── risk/
│   ├── risk_management.py        # Risk management and profit simulation module
├── sentiment/
│   ├── sentiment_analysis.py     # Sentiment analysis pipeline using Perplexity API
├── strategies/
│   ├── __init__.py               # Strategies package initializer
│   ├── trading_strategies.py     # Traditional trading strategy functions
│   ├── ensemble.py               # Ensemble decision-making module
├── utils/
│   ├── visualisation.py          # Visualization helper functions
