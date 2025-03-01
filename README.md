# StraddleAI: AI-Powered Options Trading Strategy

StraddleAI is an AI-powered trading strategy that implements a **Long Straddle Options Strategy** based on market volatility signals. It utilizes **machine learning models** to optimize trade execution and risk management.

**Key Capabilities:**

- **Real-Time Data:**  
  Fetches 1-hour intraday data from Alpha Vantage.
  
- **Technical Indicators:**  
  Computes key indicators (e.g., SMA, RSI, MACD, Bollinger Bands, ATR, VWAP, etc.) to form the feature set.
  
- **Sentiment Analysis:**  
  Uses financial sentiment analysis (via Perplexity API/FinBERT) to gauge market sentiment.
  
- **Reinforcement Learning:**  
  Employs a DQN-based RL agent to make trading decisions based on historical price and indicator data.
  
- **Transformer Ensemble:**  
  Utilizes a transformer meta-model to fuse multiple trading signals and profitability metrics, providing a final buy/sell/hold decision.
  
- **Risk Management:**  
  Implements risk controls to adjust position sizes, stop losses, and manage drawdowns.
  
- **Visualization:**  
  Generates visualizations for price trends, technical indicators, and portfolio performance.

---

## Features

- **Modular Design:**  
  Clear separation between data ingestion, processing, model training, decision-making, and risk management.
  
- **Real-Time Integration:**  
  Live intraday data fetch and dynamic updating of technical indicators.
  
- **Hybrid Decision Making:**  
  Combines outputs from an RL model, technical strategies, and a transformer-based ensemble for robust trading signals.
  
- **Risk Controls:**  
  Built-in functions for position sizing, stop-loss, take-profit, and drawdown management.
  
- **Visualization Tools:**  
  Comprehensive charts to monitor stock price trends, technical indicators, and portfolio performance.
  
- **Extensible:**  
  Easily integrate new strategies, models, or risk parameters as needed.

---

## Architecture & Directory Structure
project/
├── main.py                      # Main entry point for the pipeline
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── data/
│   ├── __init__.py
│   ├── realtime_data_pipeline.py  # Real-time data fetching & preprocessing from Alpha Vantage
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


## Front End

![image](https://github.com/user-attachments/assets/aba32ac6-d525-46dd-940d-9f2294b515df)

##  Features

- ** Stock Price Chart (24h)**  
  - Interactive line chart displaying stock price movement over the last 24 hours.
  - Time-stamped price fluctuations for better trend analysis.

- ** Real-Time Stock Data**  

- **🔎 Trade Parameters & Risk Levels**  
  - Users can assess risk levels categorized as:
    - **Low**
    - **Medium**
    - **High**
  
- **🤖 AI-Based Trade Recommendation**  
  - The model analyzes current market trends and risk tolerance to provide actionable recommendations.
  - Current suggestion: **✅ Buy NVDA**  

## UI/UX Design

- **Dark-themed interface** for a professional and trader-friendly experience.
- **Smooth data visualization** with a responsive price chart.
- **Easy-to-read financial metrics** for quick decision-making.

## Future Enhancements

- Multi-stock selection for diversified insights
- Advanced analytics & forecasting models
- User customization for personalized dashboard experience



## Installation

To install StraddleAI, follow these steps:

```sh
# Clone the repository
git clone https://github.com/yourusername/StraddleAI.git
cd StraddleAI

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Trading Bot
```sh
python main.py --mode live --config config.yaml
```

### Running Backtests
```sh
python backtest.py --strategy straddle --start-date 2023-01-01 --end-date 2023-12-31
```

### Expected Trading Simulation Output
```
INFO: Starting backtest...
INFO: Initial Portfolio Balance: $100,000
INFO: Executing Long Straddle Strategy...
INFO: Trade executed: BUY CALL 3500, BUY PUT 3500 @ Premium $X
INFO: Final Portfolio Balance: $XXX,XXX
INFO: Sharpe Ratio: [TBD]
INFO: Maximum Drawdown: [TBD]
```
*Note: Sharpe Ratio and Maximum Drawdown will be updated after full backtesting.*

## Configuration

Modify `config.yaml` to customize trading parameters, including:
```yaml
trading:
  capital: 100000
  risk_tolerance: medium
```

## Performance Metrics (Backtest Results)
| Metric             | Value |
|--------------------|-------|
| Initial Balance   | $10,000 |
| Final Balance     | $69,490.70 |
| Time | 3 years |
| Rate | 90.38% pa|

## Modules Description

### Data Pipeline

**Module:** `data/realtime_data_pipeline.py`

**Function:**  
- Fetches real-time intraday data from Alpha Vantage.

**Processing:**  
- Preprocesses the data (e.g., calculates percentage returns) and computes technical indicators like SMA_10 and RSI_14.

**Initial Data Setup:**  
- The initial data consists of AAPL stock data from January 1, 2022, to February 27, 2025, comprising 12,638 entries.  
- The model is initially trained on this data using an 80/20 train-test split.

---

### Sentiment Analysis

**Module:** `sentiment/sentiment_analysis.py`

**Function:**  
- Uses the Perplexity API (and FinBERT) for financial sentiment analysis.

**Fallback:**  
- Defaults to a neutral sentiment score if data is unavailable.

---

### RL Model

**Module:** `models/rl_model.py`

**Contents:**  
- Contains the custom `TradingEnv` class and functions to train the DQN agent.

**Helper Function:**  
- `load_or_train_rl_model` – Loads a pre-trained model if available or trains a new model and saves it.

---

### Transformer Meta-Model

**Module:** `models/transformer_model.py`

**Function:**  
- Implements a transformer-based meta-model that processes a 29-dimensional feature vector (14 strategy signals, 14 profitability metrics, and 1 sentiment score).

**Output:**  
- Provides trading decision logits and profitability estimates.

---

### Trading Strategies & Ensemble

**Modules:**  

- `strategies/trading_strategies.py`:  
  Definitions of individual trading strategy functions (e.g., momentum, mean reversion).

- `strategies/ensemble.py`:  
  Functions to compute, aggregate, and combine signals from multiple models (RL model, transformer meta-model) to generate a final ensemble decision.

---

### Risk Management

**Module:** `risk/risk_management.py`

**Function:**  
- Implements risk management functions including the computation of risk metrics (Sharpe ratio, maximum drawdown) and simulating trading with dynamic risk controls.

---

### Visualization

**Module:** `utils/visualisation.py`

**Function:**  
- Provides visualization tools to plot price charts, technical indicators, balance history, and performance metrics.

