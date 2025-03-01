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

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/StraddleAI.git
cd StraddleAI

### 2. Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

## Usage

### 1. Real-Time Data Pipeline
StraddleAI fetches 1-hour intraday data from Alpha Vantage via the module  
`data/realtime_data_pipeline.py`. This module retrieves data, preprocesses it (computing returns), and calculates technical indicators like SMA_10 and RSI_14.

### 2. Sentiment Analysis
The project includes a sentiment analysis pipeline (`sentiment/sentiment_analysis.py`) that leverages the Perplexity API and FinBERT to extract market sentiment. If no sentiment data is available, the system defaults to a neutral sentiment score.

### 3. Reinforcement Learning
The RL agent, built using Stable Baselines3 (DQN), is trained (or loaded if previously trained) on historical data. The trained model is saved to `models/trained_rl_model_final.zip` and reused to avoid retraining.

### 4. Ensemble Trading and Risk Management
The ensemble decision is made by combining signals from:
- The RL model,
- Traditional technical strategies,
- A transformer meta-model.

The risk management module (`risk/risk_management.py`) simulates the trading performance over historical data while adjusting for risk factors like stop-loss, take-profit, and maximum drawdown.


### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 5. Visualization
Visualizations are provided via functions in `utils/visualisation.py` to show trading performance, such as portfolio balance history, drawdowns, and more.

### 6. Running the Project
Execute the main pipeline by running:
```bash
python main.py

## Customization

- **Risk Parameters:**  
  Edit the `risk/risk_management.py` file to adjust the risk parameters (position size, stop-loss, take-profit, etc.) according to your trading preferences.

- **Ensemble Weights:**  
  Modify the weights in the ensemble function (`strategies/ensemble.py`) to fine-tune how much influence each component (RL, technical strategies, transformer) has on the final decision.

- **Additional Technical Indicators:**  
  Enhance the feature set by adding more technical indicators in `data/realtime_data_pipeline.py` or `data/data_pipeline.py`.

- **Sentiment Analysis Integration:**  
  Update the sentiment analysis module if you wish to use different models or API endpoints for improved sentiment extraction.



