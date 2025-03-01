AIBot - Intelligent Trading System

AIBot is an advanced, modular trading system that leverages deep learning, real-time data, and risk management to generate buy, sell, or hold signals for stock trading. The project integrates multiple components including real-time data ingestion from Alpha Vantage, sentiment analysis via Perplexity/FinBERT, a reinforcement learning (RL) agent (using DQN), and a transformer-based meta-model for ensemble decision-making. The system fuses signals from various strategies and models to provide robust trading decisions.

Table of Contents

Overview
Features
Architecture & Directory Structure
Installation
Usage
Running the Pipeline
Real-Time Data Integration
Modules Description
Data Pipeline
Sentiment Analysis
RL Model
Transformer Meta-Model
Trading Strategies and Ensemble
Risk Management
Visualization
Contributing
License
Acknowledgements
Overview

AIBot is designed to simulate and execute a trading strategy using a combination of technical analysis, machine learning, and deep learning techniques. The system is built modularly so that each component (data ingestion, sentiment analysis, RL agent, transformer, and risk management) can be independently developed, tested, and updated.

Key Capabilities:

Real-Time Data: Fetches 1-hour intraday data from Alpha Vantage.
Technical Indicators: Computes key indicators (e.g., SMA, RSI, MACD, Bollinger Bands, ATR, VWAP, etc.) to form the feature set.
Sentiment Analysis: Uses financial sentiment analysis (via Perplexity API/FinBERT) to gauge market sentiment.
Reinforcement Learning: Employs a DQN-based RL agent to make trading decisions based on historical price and indicator data.
Transformer Ensemble: Utilizes a transformer meta-model to fuse multiple trading signals and profitability metrics, providing a final buy/sell/hold decision.
Risk Management: Implements risk controls to adjust position sizes, stop losses, and manage drawdowns.
Visualization: Generates visualizations for price trends, technical indicators, and portfolio performance.
Features

Modular Design: Clear separation between data ingestion, processing, model training, decision-making, and risk management.
Real-Time Integration: Fetch live intraday data and update technical indicators dynamically.
Hybrid Decision Making: Combines outputs from an RL model, technical strategies, and a transformer-based ensemble for robust trading signals.
Risk Controls: Built-in risk management functions to simulate trading with position sizing, stop-loss, take-profit, and drawdown constraints.
Visualization Tools: Comprehensive charts to track stock price trends, technical indicators, and portfolio performance over time.
Extensible: Easily add new strategies, models, or risk parameters as needed.
Architecture & Directory Structure

project/
├── main.py                      # Main entry point for the pipeline
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── data/
│   ├── __init__.py
│   ├── realtime_data_pipeline.py  # Real-time data fetching and preprocessing from Alpha Vantage
│   └── data_pipeline.py         # (Optional) Simulated or historical data pipeline
├── models/
│   ├── __init__.py
│   ├── rl_model.py              # Custom trading environment and RL model (DQN)
│   ├── transformer_model.py     # Transformer meta-model for ensemble decision making
│   └── trained_rl_model_final.zip  # Pre-trained RL model file (if available)
├── risk/
│   ├── __init__.py
│   └── risk_management.py       # Risk management functions and simulation
├── sentiment/
│   ├── __init__.py
│   └── sentiment_analysis.py    # Sentiment analysis using Perplexity/FinBERT
├── strategies/
│   ├── __init__.py
│   ├── trading_strategies.py    # Individual technical/trading strategies
│   └── ensemble.py              # Ensemble functions combining multiple signals
└── utils/
    ├── __init__.py
    └── visualisation.py         # Visualization helpers (charts and plots)
Installation

Clone the Repository:
git clone https://github.com/YourUsername/DLWeek.git
cd DLWeek
Create a Virtual Environment:
python -m venv env
Activate the Virtual Environment:
On macOS/Linux:
source env/bin/activate
On Windows:
env\Scripts\activate
Install Dependencies:
pip install -r requirements.txt
Usage

Running the Pipeline
Run the main pipeline by executing:

python main.py
This will execute the following:

Fetch real-time 1-hour data from Alpha Vantage.
Preprocess the data and compute technical indicators.
Run sentiment analysis on the fetched data.
Load (or train) the RL model.
Simulate trading using the ensemble decision approach with risk management.
Visualize the portfolio balance history.
Real-Time Data Integration
Your real-time data is fetched via the data/realtime_data_pipeline.py module which queries Alpha Vantage for intraday (1-hour) data. The pipeline computes key technical indicators (e.g., SMA_10, RSI_14) and outputs a DataFrame that is then used throughout the rest of the system.

Modules Description

Data Pipeline
data/realtime_data_pipeline.py:
Fetches real-time intraday data from Alpha Vantage, preprocesses it (calculates percentage returns), and computes technical indicators like SMA_10 and RSI_14.
Sentiment Analysis
sentiment/sentiment_analysis.py:
Uses the Perplexity API (and FinBERT) to analyze financial news sentiment. If sentiment data isn’t available, it defaults to a neutral score.
RL Model
models/rl_model.py:
Contains your custom TradingEnv class, functions to train the DQN agent, and a helper function (load_or_train_rl_model) that loads a pre-trained model (if available) or trains a new one and saves it.
Transformer Meta-Model
models/transformer_model.py:
Implements a transformer meta-model that processes a 29-dimensional feature vector (14 strategy signals, 14 profitability metrics, and 1 sentiment score) and outputs trading decision logits and profitability estimates.
Trading Strategies & Ensemble
strategies/trading_strategies.py:
Contains definitions of individual trading strategy functions (e.g., momentum, mean reversion, etc.).
strategies/ensemble.py:
Contains functions to compute, aggregate, and combine strategy signals along with outputs from the RL model and transformer meta-model to generate a final ensemble decision.
Risk Management
risk/risk_management.py:
Contains functions to compute risk metrics (Sharpe ratio, maximum drawdown) and simulate trading with risk management constraints, dynamically adjusting position sizes, stop losses, and take profits.
Visualization
utils/visualisation.py:
Provides functions to plot price charts with technical indicators, balance history, and other performance metrics.
Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes. Ensure your code adheres to the project's style and includes tests where applicable.

License

This project is licensed under the MIT License.

Acknowledgements

Alpha Vantage for providing free real-time stock data.
Stable Baselines3 for reinforcement learning tools.
Transformers for the transformer models.
FinBERT for financial sentiment analysis.
Special thanks to all contributors and open-source projects that made this work possible.
