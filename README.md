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

## Trading Simulation Results

Our risk-managed ensemble trading strategy was backtested on a three-year dataset using 1-hour intraday data from Alpha Vantage. The system combines technical analysis, sentiment data, a reinforcement learning (RL) agent, and a transformer meta-model to generate ensemble trading decisions. Below are some key performance metrics and sample debug logs from the simulation.

### Key Metrics

- **Initial Portfolio Balance:** \$10,000  
- **Final Portfolio Balance:** \$69,490.70  
- **Total Profit:** \$59,490.70  
- **Profit Increase:** ~594.91% over the simulation period

### Debug Log Sample

Our trading bot was rigorously backtested on 3 years of historical AAPL stock data using 1-hour intraday data from Alpha Vantage. The simulation was configured with a **medium risk profile** and employed profit compounding after every trade. This means that the gains from each trade were reinvested, leading to exponential growth over time.

### Simulation Setup

- **Data Source:**  
  3 years of historical intraday data (1-hour intervals) for AAPL fetched from Alpha Vantage.

- **Risk Profile:**  
  **Medium Risk Level**  
  - **Position Size:** Approximately 7% of the portfolio is risked per trade.  
  - **Stop-Loss & Take-Profit:** Conservative thresholds are set to limit losses and secure gains, with a maximum drawdown allowance of 20%.
  - This risk level is designed to balance growth and risk exposure, avoiding overly aggressive moves while still capturing significant market opportunities.

- **Profit Compounding:**  
  The simulation compounds profits after each trade. This means that returns from successful trades are reinvested into subsequent trades, leading to a cumulative effect that accelerates portfolio growth over time.

### Performance Metrics

- **Initial Portfolio Balance:** \$10,000  
- **Final Portfolio Balance:** \$69,490.70  
- **Total Profit:** \$59,490.70  
- **Compounded Growth:** The compounding effect contributed significantly to the overall profit, as gains from each trade were reinvested to fuel further returns.
- **Sharpe Ratio:** [Insert Sharpe Ratio]  
- **Maximum Drawdown:** [Insert Maximum Drawdown]

Snipet


[DEBUG] Step=0, action=0, return=-0.3745, raw_pnl=-0.00, actual_pnl=-0.00, balance=10000.00
[DEBUG] Step=1, action=1, return=0.3463, raw_pnl=346.27, actual_pnl=105.00, balance=10105.00
[DEBUG] Step=2, action=1, return=0.0535, raw_pnl=53.51, actual_pnl=53.51, balance=10158.51
[DEBUG] Step=3, action=0, return=-0.2974, raw_pnl=-0.00, actual_pnl=-0.00, balance=10158.51
[DEBUG] Step=4, action=1, return=0.3964, raw_pnl=396.38, actual_pnl=106.66, balance=10265.18
[DEBUG] Step=5, action=0, return=-0.2086, raw_pnl=-0.00, actual_pnl=-0.00, balance=10265.18
[DEBUG] Step=6, action=1, return=0.1934, raw_pnl=193.40, actual_pnl=107.78, balance=10372.96
[DEBUG] Step=7, action=1, return=0.0007, raw_pnl=0.75, actual_pnl=0.75, balance=10373.71
[DEBUG] Step=8, action=1, return=-0.0598, raw_pnl=-59.84, actual_pnl=-50.83, balance=10322.88
[DEBUG] Step=9, action=0, return=-0.2901, raw_pnl=-0.00, actual_pnl=-0.00, balance=10322.88
[DEBUG] Step=10, action=1, return=0.6833, raw_pnl=683.32, actual_pnl=108.39, balance=10431.27
[DEBUG] Step=11, action=0, return=-0.2803, raw_pnl=-0.00, actual_pnl=-0.00, balance=10431.27
[DEBUG] Step=12, action=0, return=-0.1017, raw_pnl=-0.00, actual_pnl=-0.00, balance=10431.27
[DEBUG] Step=13, action=0, return=-0.1228, raw_pnl=-0.00, actual_pnl=-0.00, balance=10431.27
[DEBUG] Step=14, action=1, return=0.5286, raw_pnl=528.57, actual_pnl=109.53, balance=10540.80
[DEBUG] Step=15, action=1, return=0.0545, raw_pnl=54.48, actual_pnl=54.48, balance=10595.28
[DEBUG] Step=16, action=0, return=-0.3940, raw_pnl=-0.00, actual_pnl=-0.00, balance=10595.28
[DEBUG] Step=17, action=1, return=0.4874, raw_pnl=487.42, actual_pnl=111.25, balance=10706.53
[DEBUG] Step=18, action=0, return=-0.1889, raw_pnl=-0.00, actual_pnl=-0.00, balance=10706.53
[DEBUG] Step=19, action=1, return=0.3414, raw_pnl=341.36, actual_pnl=112.42, balance=10818.95
[DEBUG] Step=20, action=0, return=-0.2862, raw_pnl=-0.00, actual_pnl=-0.00, balance=10818.95
[DEBUG] Step=21, action=1, return=0.4399, raw_pnl=439.87, actual_pnl=113.60, balance=10932.55
[DEBUG] Step=22, action=1, return=-0.1799, raw_pnl=-179.90, actual_pnl=-53.57, balance=10878.98
[DEBUG] Step=23, action=1, return=0.3966, raw_pnl=396.61, actual_pnl=114.23, balance=10993.21
[DEBUG] Step=24, action=0, return=-0.4127, raw_pnl=-0.00, actual_pnl=-0.00, balance=10993.21
[DEBUG] Step=25, action=0, return=0.1789, raw_pnl=0.00, actual_pnl=0.00, balance=10993.21
[DEBUG] Step=26, action=0, return=-0.1697, raw_pnl=-0.00, actual_pnl=-0.00, balance=10993.21
[DEBUG] Step=27, action=1, return=0.7285, raw_pnl=728.55, actual_pnl=115.43, balance=11108.64
[DEBUG] Step=28, action=1, return=-0.0246, raw_pnl=-24.60, actual_pnl=-24.60, balance=11084.03
[DEBUG] Step=29, action=0, return=-0.3299, raw_pnl=-0.00, actual_pnl=-0.00, balance=11084.03
[DEBUG] Step=30, action=1, return=0.3196, raw_pnl=319.60, actual_pnl=116.38, balance=11200.42
[DEBUG] Step=31, action=1, return=0.0947, raw_pnl=94.72, actual_pnl=94.72, balance=11295.14
[DEBUG] Step=32, action=1, return=-0.1442, raw_pnl=-144.19, actual_pnl=-55.35, balance=11239.79
[DEBUG] Step=33, action=1, return=-0.0164, raw_pnl=-16.43, actual_pnl=-16.43, balance=11223.36
[DEBUG] Step=34, action=0, return=-0.1881, raw_pnl=-0.00, actual_pnl=-0.00, balance=11223.36
[DEBUG] Step=35, action=0, return=-0.1198, raw_pnl=-0.00, actual_pnl=-0.00, balance=11223.36
[DEBUG] Step=36, action=1, return=0.7356, raw_pnl=735.62, actual_pnl=117.85, balance=11341.21
[DEBUG] Step=37, action=1, return=0.0017, raw_pnl=1.69, actual_pnl=1.69, balance=11342.90
[DEBUG] Step=38, action=1, return=-0.1407, raw_pnl=-140.66, actual_pnl=-55.58, balance=11287.32
[DEBUG] Step=39, action=0, return=-0.1801, raw_pnl=-0.00, actual_pnl=-0.00, balance=11287.32
[DEBUG] Step=40, action=0, return=0.0076, raw_pnl=0.00, actual_pnl=0.00, balance=11287.32
[DEBUG] Step=41, action=1, return=0.2792, raw_pnl=279.23, actual_pnl=118.52, balance=11405.83
[DEBUG] Step=42, action=1, return=0.0992, raw_pnl=99.17, actual_pnl=99.17, balance=11505.00
[DEBUG] Step=43, action=1, return=-0.0053, raw_pnl=-5.28, actual_pnl=-5.28, balance=11499.71
[DEBUG] Step=44, action=1, return=-0.0568, raw_pnl=-56.81, actual_pnl=-56.35, balance=11443.37
[DEBUG] Step=45, action=1, return=-0.0774, raw_pnl=-77.45, actual_pnl=-56.07, balance=11387.29
[DEBUG] Step=46, action=0, return=-0.3398, raw_pnl=-0.00, actual_pnl=-0.00, balance=11387.29
[DEBUG] Step=47, action=0, return=0.0715, raw_pnl=0.00, actual_pnl=0.00, balance=11387.29
[DEBUG] Step=48, action=1, return=0.6344, raw_pnl=634.39, actual_pnl=119.57, balance=11506.86
[DEBUG] Step=49, action=1, return=-0.1539, raw_pnl=-153.87, actual_pnl=-56.38, balance=11450.48
[DEBUG] Step=50, action=0, return=-0.3718, raw_pnl=-0.00, actual_pnl=-0.00, balance=11450.48
[DEBUG] Step=51, action=0, return=0.0914, raw_pnl=0.00, actual_pnl=0.00, balance=11450.48
[DEBUG] Step=52, action=1, return=0.5103, raw_pnl=510.25, actual_pnl=120.23, balance=11570.71
[DEBUG] Step=53, action=0, return=-0.3958, raw_pnl=-0.00, actual_pnl=-0.00, balance=11570.71
[DEBUG] Step=54, action=0, return=0.1550, raw_pnl=0.00, actual_pnl=0.00, balance=11570.71
[DEBUG] Step=55, action=1, return=0.3342, raw_pnl=334.19, actual_pnl=121.49, balance=11692.20
[DEBUG] Step=56, action=1, return=0.0924, raw_pnl=92.44, actual_pnl=92.44, balance=11784.64
[DEBUG] Step=57, action=1, return=-0.0236, raw_pnl=-23.60, actual_pnl=-23.60, balance=11761.03
[DEBUG] Step=58, action=0, return=-0.2589, raw_pnl=-0.00, actual_pnl=-0.00, balance=11761.03
[DEBUG] Step=59, action=1, return=0.3985, raw_pnl=398.53, actual_pnl=123.49, balance=11884.52
[DEBUG] Step=60, action=0, return=-0.2774, raw_pnl=-0.00, actual_pnl=-0.00, balance=11884.52
[DEBUG] Step=61, action=0, return=0.0712, raw_pnl=0.00, actual_pnl=0.00, balance=11884.52
[DEBUG] Step=62, action=1, return=0.3177, raw_pnl=317.71, actual_pnl=124.79, balance=12009.31
[DEBUG] Step=63, action=1, return=-0.0555, raw_pnl=-55.46, actual_pnl=-55.46, balance=11953.85
[DEBUG] Step=64, action=1, return=0.1210, raw_pnl=120.99, actual_pnl=120.99, balance=12074.84
[DEBUG] Step=65, action=1, return=-0.1036, raw_pnl=-103.62, actual_pnl=-59.17, balance=12015.68
[DEBUG] Step=66, action=1, return=-0.0539, raw_pnl=-53.88, actual_pnl=-53.88, balance=11961.80
[DEBUG] Step=67, action=0, return=-0.3026, raw_pnl=-0.00, actual_pnl=-0.00, balance=11961.80
[DEBUG] Step=68, action=0, return=0.2506, raw_pnl=0.00, actual_pnl=0.00, balance=11961.80
[DEBUG] Step=69, action=0, return=-0.0750, raw_pnl=-0.00, actual_pnl=-0.00, balance=11961.80
[DEBUG] Step=70, action=0, return=-0.0168, raw_pnl=-0.00, actual_pnl=-0.00, balance=11961.80
[DEBUG] Step=71, action=1, return=0.5860, raw_pnl=586.03, actual_pnl=125.60, balance=12087.40
[DEBUG] Step=72, action=0, return=-0.2939, raw_pnl=-0.00, actual_pnl=-0.00, balance=12087.40
[DEBUG] Step=73, action=1, return=0.3582, raw_pnl=358.16, actual_pnl=126.92, balance=12214.32
[DEBUG] Step=74, action=1, return=-0.1379, raw_pnl=-137.90, actual_pnl=-59.85, balance=12154.47
[DEBUG] Step=75, action=1, return=0.1003, raw_pnl=100.34, actual_pnl=100.34, balance=12254.81
[DEBUG] Step=76, action=0, return=-0.1628, raw_pnl=-0.00, actual_pnl=-0.00, balance=12254.81
[DEBUG] Step=77, action=1, return=0.0494, raw_pnl=49.42, actual_pnl=49.42, balance=12304.24
[DEBUG] Step=78, action=1, return=-0.0535, raw_pnl=-53.51, actual_pnl=-53.51, balance=12250.72
[DEBUG] Step=79, action=0, return=-0.1992, raw_pnl=-0.00, actual_pnl=-0.00, balance=12250.72
[DEBUG] Step=80, action=1, return=0.4411, raw_pnl=441.09, actual_pnl=128.63, balance=12379.35
[DEBUG] Step=81, action=0, return=-0.2564, raw_pnl=-0.00, actual_pnl=-0.00, balance=12379.35
[DEBUG] Step=82, action=0, return=-0.2002, raw_pnl=-0.00, actual_pnl=-0.00, balance=12379.35
[DEBUG] Step=83, action=1, return=0.6064, raw_pnl=606.41, actual_pnl=129.98, balance=12509.34
[DEBUG] Step=84, action=0, return=-0.2846, raw_pnl=-0.00, actual_pnl=-0.00, balance=12509.34
[DEBUG] Step=85, action=1, return=0.6485, raw_pnl=648.49, actual_pnl=131.35, balance=12640.69
[DEBUG] Step=86, action=1, return=0.0069, raw_pnl=6.94, actual_pnl=6.94, balance=12647.63
[DEBUG] Step=87, action=1, return=-0.0200, raw_pnl=-19.99, actual_pnl=-19.99, balance=12627.63
[DEBUG] Step=88, action=0, return=-0.2845, raw_pnl=-0.00, actual_pnl=-0.00, balance=12627.63
[DEBUG] Step=89, action=0, return=-0.2589, raw_pnl=-0.00, actual_pnl=-0.00, balance=12627.63
[DEBUG] Step=90, action=1, return=0.8990, raw_pnl=898.97, actual_pnl=132.59, balance=12760.22
[DEBUG] Step=91, action=0, return=-0.2594, raw_pnl=-0.00, actual_pnl=-0.00, balance=12760.22
[DEBUG] Step=92, action=1, return=0.3770, raw_pnl=377.03, actual_pnl=133.98, balance=12894.21
[DEBUG] Step=93, action=1, return=-0.0015, raw_pnl=-1.54, actual_pnl=-1.54, balance=12892.66
[DEBUG] Step=94, action=1, return=-0.0563, raw_pnl=-56.33, actual_pnl=-56.33, balance=12836.33
[DEBUG] Step=95, action=0, return=-0.3014, raw_pnl=-0.00, actual_pnl=-0.00, balance=12836.33
[DEBUG] Step=96, action=0, return=0.0700, raw_pnl=0.00, actual_pnl=0.00, balance=12836.33
[DEBUG] Step=97, action=1, return=0.3365, raw_pnl=336.47, actual_pnl=134.78, balance=12971.12
[DEBUG] Step=98, action=0, return=-0.2886, raw_pnl=-0.00, actual_pnl=-0.00, balance=12971.12
[DEBUG] Step=99, action=0, return=-0.1119, raw_pnl=-0.00, actual_pnl=-0.00, balance=12971.12
[DEBUG] Step=100, action=1, return=0.3312, raw_pnl=331.18, actual_pnl=136.20, balance=13107.31
[DEBUG] Step=101, action=1, return=0.2437, raw_pnl=243.67, actual_pnl=137.63, balance=13244.94
[DEBUG] Step=102, action=1, return=-0.1240, raw_pnl=-124.02, actual_pnl=-64.90, balance=13180.04
[DEBUG] Step=103, action=0, return=-0.0743, raw_pnl=-0.00, actual_pnl=-0.00, balance=13180.04
[DEBUG] Step=104, action=0, return=-0.3012, raw_pnl=-0.00, actual_pnl=-0.00, balance=13180.04
[DEBUG] Step=105, action=1, return=0.4720, raw_pnl=471.97, actual_pnl=138.39, balance=13318.43
[DEBUG] Step=106, action=1, return=0.2322, raw_pnl=232.23, actual_pnl=139.84, balance=13458.27
[DEBUG] Step=107, action=0, return=-0.4271, raw_pnl=-0.00, actual_pnl=-0.00, balance=13458.27
[DEBUG] Step=108, action=1, return=0.3318, raw_pnl=331.77, actual_pnl=141.31, balance=13599.58
[DEBUG] Step=109, action=1, return=0.2365, raw_pnl=236.47, actual_pnl=142.80, balance=13742.38
[DEBUG] Step=110, action=1, return=-0.0728, raw_pnl=-72.76, actual_pnl=-67.34, balance=13675.04
[DEBUG] Step=111, action=1, return=-0.0251, raw_pnl=-25.13, actual_pnl=-25.13, balance=13649.91
[DEBUG] Step=112, action=1, return=0.0032, raw_pnl=3.22, actual_pnl=3.22, balance=13653.13
[DEBUG] Step=113, action=0, return=-0.2015, raw_pnl=-0.00, actual_pnl=-0.00, balance=13653.13
[DEBUG] Step=114, action=0, return=-0.0485, raw_pnl=-0.00, actual_pnl=-0.00, balance=13653.13
[DEBUG] Step=115, action=1, return=0.3987, raw_pnl=398.71, actual_pnl=143.36, balance=13796.49
[DEBUG] Step=116, action=1, return=0.0004, raw_pnl=0.42, actual_pnl=0.42, balance=13796.90
[DEBUG] Step=117, action=1, return=0.0315, raw_pnl=31.47, actual_pnl=31.47, balance=13828.37
[DEBUG] Step=118, action=1, return=0.0247, raw_pnl=24.73, actual_pnl=24.73, balance=13853.10
[DEBUG] Step=119, action=0, return=-0.2101, raw_pnl=-0.00, actual_pnl=-0.00, balance=13853.10
[DEBUG] Step=120, action=0, return=-0.0065, raw_pnl=-0.00, actual_pnl=-0.00, balance=13853.10
[DEBUG] Step=121, action=1, return=0.1977, raw_pnl=197.65, actual_pnl=145.46, balance=13998.56
[DEBUG] Step=122, action=1, return=-0.0825, raw_pnl=-82.48, actual_pnl=-68.59, balance=13929.96
[DEBUG] Step=123, action=1, return=0.0315, raw_pnl=31.52, actual_pnl=31.52, balance=13961.48
[DEBUG] Step=124, action=1, return=0.0551, raw_pnl=55.13, actual_pnl=55.13, balance=14016.61
[DEBUG] Step=125, action=1, return=0.0525, raw_pnl=52.46, actual_pnl=52.46, balance=14069.07
[DEBUG] Step=126, action=0, return=-0.2921, raw_pnl=-0.00, actual_pnl=-0.00, balance=14069.07
[DEBUG] Step=127, action=0, return=0.0281, raw_pnl=0.00, actual_pnl=0.00, balance=14069.07
[DEBUG] Step=128, action=0, return=-0.2047, raw_pnl=-0.00, actual_pnl=-0.00, balance=14069.07
[DEBUG] Step=129, action=1, return=0.4427, raw_pnl=442.69, actual_pnl=147.73, balance=14216.80
[DEBUG] Step=130, action=0, return=-0.3436, raw_pnl=-0.00, actual_pnl=-0.00, balance=14216.80
[DEBUG] Step=131, action=0, return=0.4147, raw_pnl=0.00, actual_pnl=0.00, balance=14216.80
[DEBUG] Step=132, action=1, return=0.0526, raw_pnl=52.57, actual_pnl=52.57, balance=14269.37
[DEBUG] Step=133, action=0, return=-0.1660, raw_pnl=-0.00, actual_pnl=-0.00, balance=14269.37
[DEBUG] Step=134, action=1, return=0.2365, raw_pnl=236.52, actual_pnl=149.83, balance=14419.20
[DEBUG] Step=135, action=0, return=-0.3522, raw_pnl=-0.00, actual_pnl=-0.00, balance=14419.20
[DEBUG] Step=136, action=0, return=0.0066, raw_pnl=0.00, actual_pnl=0.00, balance=14419.20
[DEBUG] Step=137, action=1, return=0.7570, raw_pnl=756.98, actual_pnl=151.40, balance=14570.60
[DEBUG] Step=138, action=1, return=-0.2537, raw_pnl=-253.71, actual_pnl=-71.40, balance=14499.20
[DEBUG] Step=139, action=0, return=-0.1714, raw_pnl=-0.00, actual_pnl=-0.00, balance=14499.20
[DEBUG] Step=140, action=1, return=0.3506, raw_pnl=350.63, actual_pnl=152.24, balance=14651.44
[DEBUG] Step=141, action=1, return=0.1628, raw_pnl=162.75, actual_pnl=153.84, balance=14805.28
[DEBUG] Step=142, action=0, return=-0.3131, raw_pnl=-0.00, actual_pnl=-0.00, balance=14805.28
[DEBUG] Step=143, action=1, return=0.3348, raw_pnl=334.81, actual_pnl=155.46, balance=14960.74
[DEBUG] Step=144, action=0, return=-0.3312, raw_pnl=-0.00, actual_pnl=-0.00, balance=14960.74
[DEBUG] Step=145, action=0, return=-0.0310, raw_pnl=-0.00, actual_pnl=-0.00, balance=14960.74
[DEBUG] Step=146, action=1, return=0.4561, raw_pnl=456.10, actual_pnl=157.09, balance=15117.83
[DEBUG] Step=147, action=1, return=0.0061, raw_pnl=6.06, actual_pnl=6.06, balance=15123.89
[DEBUG] Step=148, action=1, return=0.0628, raw_pnl=62.83, actual_pnl=62.83, balance=15186.71
[DEBUG] Step=149, action=1, return=0.0541, raw_pnl=54.15, actual_pnl=54.15, balance=15240.86
[DEBUG] Step=150, action=1, return=0.1447, raw_pnl=144.70, actual_pnl=144.70, balance=15385.56
[DEBUG] Step=151, action=1, return=-0.2326, raw_pnl=-232.58, actual_pnl=-75.39, balance=15310.17
[DEBUG] Step=152, action=0, return=-0.1275, raw_pnl=-0.00, actual_pnl=-0.00, balance=15310.17
[DEBUG] Step=153, action=1, return=0.3570, raw_pnl=356.95, actual_pnl=160.76, balance=15470.93
[DEBUG] Step=154, action=0, return=-0.2921, raw_pnl=-0.00, actual_pnl=-0.00, balance=15470.93
[DEBUG] Step=155, action=1, return=0.1323, raw_pnl=132.31, actual_pnl=132.31, balance=15603.23
[DEBUG] Step=156, action=0, return=-0.2505, raw_pnl=-0.00, actual_pnl=-0.00, balance=15603.23
[DEBUG] Step=157, action=0, return=-0.0492, raw_pnl=-0.00, actual_pnl=-0.00, balance=15603.23
[DEBUG] Step=158, action=1, return=0.9141, raw_pnl=914.12, actual_pnl=163.83, balance=15767.07
[DEBUG] Step=159, action=1, return=-0.0645, raw_pnl=-64.54, actual_pnl=-64.54, balance=15702.53
[DEBUG] Step=160, action=1, return=-0.0763, raw_pnl=-76.26, actual_pnl=-76.26, balance=15626.27
[DEBUG] Step=161, action=0, return=-0.1692, raw_pnl=-0.00, actual_pnl=-0.00, balance=15626.27
[DEBUG] Step=162, action=0, return=-0.1673, raw_pnl=-0.00, actual_pnl=-0.00, balance=15626.27
[DEBUG] Step=163, action=0, return=-0.0144, raw_pnl=-0.00, actual_pnl=-0.00, balance=15626.27
[DEBUG] Step=164, action=0, return=0.0811, raw_pnl=0.00, actual_pnl=0.00, balance=15626.27
[DEBUG] Step=165, action=1, return=0.2391, raw_pnl=239.14, actual_pnl=164.08, balance=15790.35
[DEBUG] Step=166, action=1, return=0.1067, raw_pnl=106.74, actual_pnl=106.74, balance=15897.09
[DEBUG] Step=167, action=1, return=-0.0317, raw_pnl=-31.73, actual_pnl=-31.73, balance=15865.36
[DEBUG] Step=168, action=0, return=-0.2290, raw_pnl=-0.00, actual_pnl=-0.00, balance=15865.36
[DEBUG] Step=169, action=1, return=0.5273, raw_pnl=527.32, actual_pnl=166.59, balance=16031.95
[DEBUG] Step=170, action=1, return=-0.1110, raw_pnl=-110.99, actual_pnl=-78.56, balance=15953.39
[DEBUG] Step=171, action=1, return=-0.1056, raw_pnl=-105.61, actual_pnl=-78.17, balance=15875.22
[DEBUG] Step=172, action=1, return=0.0369, raw_pnl=36.91, actual_pnl=36.91, balance=15912.13
[DEBUG] Step=173, action=0, return=-0.1192, raw_pnl=-0.00, actual_pnl=-0.00, balance=15912.13
[DEBUG] Step=174, action=0, return=-0.1211, raw_pnl=-0.00, actual_pnl=-0.00, balance=15912.13
[DEBUG] Step=175, action=0, return=0.0868, raw_pnl=0.00, actual_pnl=0.00, balance=15912.13
[DEBUG] Step=176, action=1, return=0.2964, raw_pnl=296.37, actual_pnl=167.08, balance=16079.20
[DEBUG] Step=177, action=0, return=-0.4229, raw_pnl=-0.00, actual_pnl=-0.00, balance=16079.20
[DEBUG] Step=178, action=0, return=0.1002, raw_pnl=0.00, actual_pnl=0.00, balance=16079.20
[DEBUG] Step=179, action=0, return=-0.0628, raw_pnl=-0.00, actual_pnl=-0.00, balance=16079.20
[DEBUG] Step=180, action=0, return=-0.0050, raw_pnl=-0.00, actual_pnl=-0.00, balance=16079.20
[DEBUG] Step=181, action=1, return=0.7828, raw_pnl=782.85, actual_pnl=168.83, balance=16248.04
[DEBUG] Step=182, action=1, return=-0.0818, raw_pnl=-81.81, actual_pnl=-79.62, balance=16168.42
[DEBUG] Step=183, action=1, return=-0.1347, raw_pnl=-134.70, actual_pnl=-79.23, balance=16089.20
[DEBUG] Step=184, action=0, return=-0.2553, raw_pnl=-0.00, actual_pnl=-0.00, balance=16089.20
[DEBUG] Step=185, action=1, return=0.3587, raw_pnl=358.69, actual_pnl=168.94, balance=16258.13
[DEBUG] Step=186, action=1, return=-0.0122, raw_pnl=-12.16, actual_pnl=-12.16, balance=16245.97
[DEBUG] Step=187, action=0, return=-0.2038, raw_pnl=-0.00, actual_pnl=-0.00, balance=16245.97
[DEBUG] Step=188, action=1, return=0.2222, raw_pnl=222.17, actual_pnl=170.58, balance=16416.55
[DEBUG] Step=189, action=1, return=-0.0247, raw_pnl=-24.65, actual_pnl=-24.65, balance=16391.90
[DEBUG] Step=190, action=1, return=0.1554, raw_pnl=155.41, actual_pnl=155.41, balance=16547.31
[DEBUG] Step=191, action=1, return=0.0119, raw_pnl=11.91, actual_pnl=11.91, balance=16559.22
[DEBUG] Step=192, action=0, return=-0.3607, raw_pnl=-0.00, actual_pnl=-0.00, balance=16559.22
[DEBUG] Step=193, action=1, return=0.3150, raw_pnl=315.04, actual_pnl=173.87, balance=16733.09
[DEBUG] Step=194, action=1, return=0.1828, raw_pnl=182.78, actual_pnl=175.70, balance=16908.79
[DEBUG] Step=195, action=1, return=-0.0755, raw_pnl=-75.48, actual_pnl=-75.48, balance=16833.31
[DEBUG] Step=196, action=1, return=0.2351, raw_pnl=235.08, actual_pnl=176.75, balance=17010.06
[DEBUG] Step=197, action=1, return=-0.1065, raw_pnl=-106.54, actual_pnl=-83.35, balance=16926.71
[DEBUG] Step=198, action=0, return=-0.2989, raw_pnl=-0.00, actual_pnl=-0.00, balance=16926.71
[DEBUG] Step=199, action=0, return=-0.0794, raw_pnl=-0.00, actual_pnl=-0.00, balance=16926.71
[DEBUG] Step=200, action=1, return=0.5342, raw_pnl=534.16, actual_pnl=177.73, balance=17104.44
[DEBUG] Step=201, action=0, return=-0.3750, raw_pnl=-0.00, actual_pnl=-0.00, balance=17104.44
[DEBUG] Step=202, action=1, return=0.5448, raw_pnl=544.82, actual_pnl=179.60, balance=17284.04
[DEBUG] Step=203, action=1, return=0.2235, raw_pnl=223.52, actual_pnl=181.48, balance=17465.52
[DEBUG] Step=204, action=1, return=-0.1880, raw_pnl=-188.00, actual_pnl=-85.58, balance=17379.94
[DEBUG] Step=205, action=0, return=-0.1189, raw_pnl=-0.00, actual_pnl=-0.00, balance=17379.94
[DEBUG] Step=206, action=1, return=0.1838, raw_pnl=183.78, actual_pnl=182.49, balance=17562.43
[DEBUG] Step=207, action=1, return=-0.1126, raw_pnl=-112.60, actual_pnl=-86.06, balance=17476.37
[DEBUG] Step=208, action=1, return=0.0599, raw_pnl=59.91, actual_pnl=59.91, balance=17536.28
[DEBUG] Step=209, action=1, return=0.2561, raw_pnl=256.11, actual_pnl=184.13, balance=17720.41
[DEBUG] Step=210, action=0, return=-0.2861, raw_pnl=-0.00, actual_pnl=-0.00, balance=17720.41
[DEBUG] Step=211, action=1, return=0.4149, raw_pnl=414.90, actual_pnl=186.06, balance=17906.48
[DEBUG] Step=212, action=1, return=-0.0285, raw_pnl=-28.47, actual_pnl=-28.47, balance=17878.00
[DEBUG] Step=213, action=0, return=-0.3724, raw_pnl=-0.00, actual_pnl=-0.00, balance=17878.00
[DEBUG] Step=214, action=0, return=-0.1057, raw_pnl=-0.00, actual_pnl=-0.00, balance=17878.00
[DEBUG] Step=215, action=0, return=0.0294, raw_pnl=0.00, actual_pnl=0.00, balance=17878.00
[DEBUG] Step=216, action=0, return=-0.0750, raw_pnl=-0.00, actual_pnl=-0.00, balance=17878.00
[DEBUG] Step=217, action=0, return=0.0749, raw_pnl=0.00, actual_pnl=0.00, balance=17878.00
[DEBUG] Step=218, action=1, return=0.5378, raw_pnl=537.77, actual_pnl=187.72, balance=18065.72
[DEBUG] Step=219, action=0, return=-0.3635, raw_pnl=-0.00, actual_pnl=-0.00, balance=18065.72
[DEBUG] Step=220, action=0, return=0.2313, raw_pnl=0.00, actual_pnl=0.00, balance=18065.72
[DEBUG] Step=221, action=1, return=0.3987, raw_pnl=398.72, actual_pnl=189.69, balance=18255.41
[DEBUG] Step=222, action=0, return=-0.4453, raw_pnl=-0.00, actual_pnl=-0.00, balance=18255.41
[DEBUG] Step=223, action=1, return=0.7732, raw_pnl=773.20, actual_pnl=191.68, balance=18447.09
[DEBUG] Step=224, action=0, return=-0.2935, raw_pnl=-0.00, actual_pnl=-0.00, balance=18447.09
[DEBUG] Step=225, action=0, return=-0.1277, raw_pnl=-0.00, actual_pnl=-0.00, balance=18447.09
[DEBUG] Step=226, action=1, return=0.5174, raw_pnl=517.43, actual_pnl=193.69, balance=18640.79
[DEBUG] Step=227, action=1, return=-0.0400, raw_pnl=-39.96, actual_pnl=-39.96, balance=18600.83
[DEBUG] Step=228, action=1, return=0.1526, raw_pnl=152.57, actual_pnl=152.57, balance=18753.40
[DEBUG] Step=229, action=1, return=-0.0758, raw_pnl=-75.85, actual_pnl=-75.85, balance=18677.56
[DEBUG] Step=230, action=1, return=0.0394, raw_pnl=39.43, actual_pnl=39.43, balance=18716.98
[DEBUG] Step=231, action=0, return=-0.2891, raw_pnl=-0.00, actual_pnl=-0.00, balance=18716.98
[DEBUG] Step=232, action=0, return=-0.0816, raw_pnl=-0.00, actual_pnl=-0.00, balance=18716.98
[DEBUG] Step=233, action=1, return=0.4868, raw_pnl=486.80, actual_pnl=196.53, balance=18913.51
[DEBUG] Step=234, action=1, return=0.0321, raw_pnl=32.11, actual_pnl=32.11, balance=18945.63
[DEBUG] Step=235, action=1, return=0.1017, raw_pnl=101.65, actual_pnl=101.65, balance=19047.28
[DEBUG] Step=236, action=0, return=-0.2903, raw_pnl=-0.00, actual_pnl=-0.00, balance=19047.28
[DEBUG] Step=237, action=0, return=-0.0287, raw_pnl=-0.00, actual_pnl=-0.00, balance=19047.28
[DEBUG] Step=238, action=1, return=0.2947, raw_pnl=294.74, actual_pnl=200.00, balance=19247.28
[DEBUG] Step=239, action=0, return=-0.2452, raw_pnl=-0.00, actual_pnl=-0.00, balance=19247.28
[DEBUG] Step=240, action=1, return=0.4400, raw_pnl=440.00, actual_pnl=202.10, balance=19449.37
[DEBUG] Step=241, action=1, return=-0.0375, raw_pnl=-37.47, actual_pnl=-37.47, balance=19411.90
[DEBUG] Step=242, action=0, return=-0.2311, raw_pnl=-0.00, actual_pnl=-0.00, balance=19411.90
[DEBUG] Step=243, action=1, return=0.2252, raw_pnl=225.25, actual_pnl=203.82, balance=19615.73
[DEBUG] Step=244, action=1, return=0.0021, raw_pnl=2.10, actual_pnl=2.10, balance=19617.83
[DEBUG] Step=245, action=0, return=-0.3713, raw_pnl=-0.00, actual_pnl=-0.00, balance=19617.83
[DEBUG] Step=246, action=1, return=0.7247, raw_pnl=724.70, actual_pnl=205.99, balance=19823.81
[DEBUG] Step=247, action=0, return=-0.2088, raw_pnl=-0.00, actual_pnl=-0.00, balance=19823.81
[DEBUG] Step=248, action=1, return=0.2134, raw_pnl=213.39, actual_pnl=208.15, balance=20031.96
[DEBUG] Step=249, action=0, return=-0.2773, raw_pnl=-0.00, actual_pnl=-0.00, balance=20031.96
[DEBUG] Step=250, action=1, return=0.4359, raw_pnl=435.95, actual_pnl=210.34, balance=20242.30
[DEBUG] Step=251, action=0, return=-0.2671, raw_pnl=-0.00, actual_pnl=-0.00, balance=20242.30
[DEBUG] Step=252, action=0, return=-0.2724, raw_pnl=-0.00, actual_pnl=-0.00, balance=20242.30
[DEBUG] Step=253, action=1, return=0.8850, raw_pnl=884.95, actual_pnl=212.54, balance=20454.84
[DEBUG] Step=254, action=0, return=-0.4273, raw_pnl=-0.00, actual_pnl=-0.00, balance=20454.84
[DEBUG] Step=255, action=0, return=0.2090, raw_pnl=0.00, actual_pnl=0.00, balance=20454.84
[DEBUG] Step=256, action=1, return=0.4781, raw_pnl=478.09, actual_pnl=214.78, balance=20669.62
[DEBUG] Step=257, action=1, return=0.0003, raw_pnl=0.28, actual_pnl=0.28, balance=20669.90
[DEBUG] Step=258, action=1, return=-0.1934, raw_pnl=-193.36, actual_pnl=-101.28, balance=20568.62
[DEBUG] Step=259, action=1, return=0.0371, raw_pnl=37.12, actual_pnl=37.12, balance=20605.73
[DEBUG] Step=260, action=0, return=-0.1124, raw_pnl=-0.00, actual_pnl=-0.00, balance=20605.73
[DEBUG] Step=261, action=0, return=-0.1072, raw_pnl=-0.00, actual_pnl=-0.00, balance=20605.73
[DEBUG] Step=262, action=0, return=0.0274, raw_pnl=0.00, actual_pnl=0.00, balance=20605.73
[DEBUG] Step=263, action=1, return=0.2588, raw_pnl=258.80, actual_pnl=216.36, balance=20822.09
[DEBUG] Step=264, action=1, return=0.0477, raw_pnl=47.75, actual_pnl=47.75, balance=20869.84
[DEBUG] Step=265, action=1, return=0.0224, raw_pnl=22.37, actual_pnl=22.37, balance=20892.21
[DEBUG] Step=266, action=1, return=-0.0011, raw_pnl=-1.09, actual_pnl=-1.09, balance=20891.11
[DEBUG] Step=267, action=0, return=-0.3903, raw_pnl=-0.00, actual_pnl=-0.00, balance=20891.11
[DEBUG] Step=268, action=0, return=0.3695, raw_pnl=0.00, actual_pnl=0.00, balance=20891.11
[DEBUG] Step=269, action=0, return=-0.2923, raw_pnl=-0.00, actual_pnl=-0.00, balance=20891.11
[DEBUG] Step=270, action=1, return=0.4652, raw_pnl=465.19, actual_pnl=219.36, balance=21110.47
[DEBUG] Step=271, action=1, return=-0.0697, raw_pnl=-69.70, actual_pnl=-69.70, balance=21040.77
[DEBUG] Step=272, action=1, return=0.3095, raw_pnl=309.51, actual_pnl=220.93, balance=21261.70
[DEBUG] Step=273, action=0, return=-0.2844, raw_pnl=-0.00, actual_pnl=-0.00, balance=21261.70
[DEBUG] Step=274, action=0, return=-0.1731, raw_pnl=-0.00, actual_pnl=-0.00, balance=21261.70
[DEBUG] Step=275, action=0, return=0.0232, raw_pnl=0.00, actual_pnl=0.00, balance=21261.70
[DEBUG] Step=276, action=1, return=0.5411, raw_pnl=541.14, actual_pnl=223.25, balance=21484.95
[DEBUG] Step=277, action=1, return=-0.0813, raw_pnl=-81.35, actual_pnl=-81.35, balance=21403.60
[DEBUG] Step=278, action=0, return=-0.3195, raw_pnl=-0.00, actual_pnl=-0.00, balance=21403.60
[DEBUG] Step=279, action=0, return=-0.0155, raw_pnl=-0.00, actual_pnl=-0.00, balance=21403.60
[DEBUG] Step=280, action=1, return=0.5690, raw_pnl=569.01, actual_pnl=224.74, balance=21628.34
[DEBUG] Step=281, action=0, return=-0.3693, raw_pnl=-0.00, actual_pnl=-0.00, balance=21628.34
[DEBUG] Step=282, action=1, return=0.6983, raw_pnl=698.29, actual_pnl=227.10, balance=21855.44
[DEBUG] Step=283, action=1, return=-0.0635, raw_pnl=-63.46, actual_pnl=-63.46, balance=21791.98
[DEBUG] Step=284, action=0, return=-0.3662, raw_pnl=-0.00, actual_pnl=-0.00, balance=21791.98
[DEBUG] Step=285, action=0, return=0.0032, raw_pnl=0.00, actual_pnl=0.00, balance=21791.98
[DEBUG] Step=286, action=1, return=0.8313, raw_pnl=831.28, actual_pnl=228.82, balance=22020.79
[DEBUG] Step=287, action=1, return=-0.3082, raw_pnl=-308.24, actual_pnl=-107.90, balance=21912.89
[DEBUG] Step=288, action=0, return=-0.0026, raw_pnl=-0.00, actual_pnl=-0.00, balance=21912.89
[DEBUG] Step=289, action=1, return=0.3226, raw_pnl=322.59, actual_pnl=230.09, balance=22142.98
[DEBUG] Step=290, action=1, return=0.0742, raw_pnl=74.17, actual_pnl=74.17, balance=22217.14
[DEBUG] Step=291, action=1, return=0.0199, raw_pnl=19.90, actual_pnl=19.90, balance=22237.04
[DEBUG] Step=292, action=1, return=-0.1171, raw_pnl=-117.13, actual_pnl=-108.96, balance=22128.08
[DEBUG] Step=293, action=0, return=-0.2151, raw_pnl=-0.00, actual_pnl=-0.00, balance=22128.08
[DEBUG] Step=294, action=0, return=-0.2127, raw_pnl=-0.00, actual_pnl=-0.00, balance=22128.08
[DEBUG] Step=295, action=1, return=0.6402, raw_pnl=640.19, actual_pnl=232.34, balance=22360.43
[DEBUG] Step=296, action=1, return=-0.1231, raw_pnl=-123.09, actual_pnl=-109.57, balance=22250.86
[DEBUG] Step=297, action=0, return=-0.0861, raw_pnl=-0.00, actual_pnl=-0.00, balance=22250.86
[DEBUG] Step=298, action=1, return=0.3385, raw_pnl=338.52, actual_pnl=233.63, balance=22484.50
[DEBUG] Step=299, action=0, return=-0.4171, raw_pnl=-0.00, actual_pnl=-0.00, balance=22484.50
[DEBUG] Step=300, action=0, return=0.3433, raw_pnl=0.00, actual_pnl=0.00, balance=22484.50
[DEBUG] Step=301, action=0, return=-0.3224, raw_pnl=-0.00, actual_pnl=-0.00, balance=22484.50
[DEBUG] Step=302, action=0, return=0.4522, raw_pnl=0.00, actual_pnl=0.00, balance=22484.50
[DEBUG] Step=303, action=0, return=-0.2808, raw_pnl=-0.00, actual_pnl=-0.00, balance=22484.50
[DEBUG] Step=304, action=0, return=0.0592, raw_pnl=0.00, actual_pnl=0.00, balance=22484.50
[DEBUG] Step=305, action=0, return=-0.0012, raw_pnl=-0.00, actual_pnl=-0.00, balance=22484.50
[DEBUG] Step=306, action=1, return=0.4758, raw_pnl=475.77, actual_pnl=236.09, balance=22720.58
[DEBUG] Step=307, action=1, return=0.0587, raw_pnl=58.72, actual_pnl=58.72, balance=22779.30
[DEBUG] Step=308, action=1, return=-0.0932, raw_pnl=-93.17, actual_pnl=-93.17, balance=22686.13
[DEBUG] Step=309, action=1, return=0.2392, raw_pnl=239.24, actual_pnl=238.20, balance=22924.33
[DEBUG] Step=310, action=0, return=-0.2993, raw_pnl=-0.00, actual_pnl=-0.00, balance=22924.33
[DEBUG] Step=311, action=0, return=-0.0648, raw_pnl=-0.00, actual_pnl=-0.00, balance=22924.33
[DEBUG] Step=312, action=1, return=0.4534, raw_pnl=453.36, actual_pnl=240.71, balance=23165.04
[DEBUG] Step=313, action=0, return=-0.3452, raw_pnl=-0.00, actual_pnl=-0.00, balance=23165.04
[DEBUG] Step=314, action=1, return=0.6045, raw_pnl=604.47, actual_pnl=243.23, balance=23408.27
[DEBUG] Step=315, action=0, return=-0.4844, raw_pnl=-0.00, actual_pnl=-0.00, balance=23408.27
[DEBUG] Step=316, action=1, return=0.9462, raw_pnl=946.22, actual_pnl=245.79, balance=23654.06
[DEBUG] Step=317, action=0, return=-0.4704, raw_pnl=-0.00, actual_pnl=-0.00, balance=23654.06
[DEBUG] Step=318, action=1, return=0.8129, raw_pnl=812.90, actual_pnl=248.37, balance=23902.43
[DEBUG] Step=319, action=1, return=-0.1922, raw_pnl=-192.18, actual_pnl=-117.12, balance=23785.31
[DEBUG] Step=320, action=1, return=0.3046, raw_pnl=304.55, actual_pnl=249.75, balance=24035.05
[DEBUG] Step=321, action=0, return=-0.4612, raw_pnl=-0.00, actual_pnl=-0.00, balance=24035.05
[DEBUG] Step=322, action=1, return=0.4471, raw_pnl=447.07, actual_pnl=252.37, balance=24287.42
[DEBUG] Step=323, action=1, return=0.2674, raw_pnl=267.37, actual_pnl=255.02, balance=24542.44
[DEBUG] Step=324, action=1, return=-0.2266, raw_pnl=-226.58, actual_pnl=-120.26, balance=24422.18
[DEBUG] Step=325, action=1, return=0.0698, raw_pnl=69.79, actual_pnl=69.79, balance=24491.97
[DEBUG] Step=326, action=1, return=0.0407, raw_pnl=40.72, actual_pnl=40.72, balance=24532.69
[DEBUG] Step=327, action=0, return=-0.1422, raw_pnl=-0.00, actual_pnl=-0.00, balance=24532.69
[DEBUG] Step=328, action=1, return=0.1189, raw_pnl=118.95, actual_pnl=118.95, balance=24651.64
[DEBUG] Step=329, action=1, return=-0.0266, raw_pnl=-26.57, actual_pnl=-26.57, balance=24625.07
[DEBUG] Step=330, action=1, return=0.2000, raw_pnl=199.99, actual_pnl=199.99, balance=24825.06
[DEBUG] Step=331, action=0, return=-0.4501, raw_pnl=-0.00, actual_pnl=-0.00, balance=24825.06
[DEBUG] Step=332, action=0, return=0.2253, raw_pnl=0.00, actual_pnl=0.00, balance=24825.06
[DEBUG] Step=333, action=1, return=0.5226, raw_pnl=522.61, actual_pnl=260.66, balance=25085.72
[DEBUG] Step=334, action=1, return=-0.0308, raw_pnl=-30.84, actual_pnl=-30.84, balance=25054.89
[DEBUG] Step=335, action=0, return=-0.2299, raw_pnl=-0.00, actual_pnl=-0.00, balance=25054.89
[DEBUG] Step=336, action=1, return=0.1130, raw_pnl=112.99, actual_pnl=112.99, balance=25167.88
[DEBUG] Step=337, action=0, return=-0.2116, raw_pnl=-0.00, actual_pnl=-0.00, balance=25167.88
[DEBUG] Step=338, action=0, return=-0.0699, raw_pnl=-0.00, actual_pnl=-0.00, balance=25167.88
[DEBUG] Step=339, action=0, return=0.2319, raw_pnl=0.00, actual_pnl=0.00, balance=25167.88
[DEBUG] Step=340, action=0, return=-0.0754, raw_pnl=-0.00, actual_pnl=-0.00, balance=25167.88
[DEBUG] Step=341, action=1, return=0.1702, raw_pnl=170.17, actual_pnl=170.17, balance=25338.05
[DEBUG] Step=342, action=0, return=-0.3195, raw_pnl=-0.00, actual_pnl=-0.00, balance=25338.05
[DEBUG] Step=343, action=1, return=0.8320, raw_pnl=831.99, actual_pnl=266.05, balance=25604.10
[DEBUG] Step=344, action=1, return=0.0060, raw_pnl=5.98, actual_pnl=5.98, balance=25610.08
[DEBUG] Step=345, action=1, return=-0.1450, raw_pnl=-145.02, actual_pnl=-125.49, balance=25484.59
[DEBUG] Step=346, action=1, return=-0.0954, raw_pnl=-95.44, actual_pnl=-95.44, balance=25389.16
[DEBUG] Step=347, action=0, return=-0.1475, raw_pnl=-0.00, actual_pnl=-0.00, balance=25389.16
[DEBUG] Step=348, action=1, return=0.3851, raw_pnl=385.08, actual_pnl=266.59, balance=25655.74
[DEBUG] Step=349, action=1, return=-0.0712, raw_pnl=-71.16, actual_pnl=-71.16, balance=25584.59
[DEBUG] Step=350, action=0, return=-0.3099, raw_pnl=-0.00, actual_pnl=-0.00, balance=25584.59
[DEBUG] Step=351, action=1, return=0.6436, raw_pnl=643.64, actual_pnl=268.64, balance=25853.23
[DEBUG] Step=352, action=1, return=-0.0463, raw_pnl=-46.26, actual_pnl=-46.26, balance=25806.97
[DEBUG] Step=353, action=1, return=0.0698, raw_pnl=69.83, actual_pnl=69.83, balance=25876.80
[DEBUG] Step=354, action=1, return=-0.1149, raw_pnl=-114.92, actual_pnl=-114.92, balance=25761.87
[DEBUG] Step=355, action=1, return=-0.0651, raw_pnl=-65.08, actual_pnl=-65.08, balance=25696.80
[DEBUG] Step=356, action=0, return=-0.1210, raw_pnl=-0.00, actual_pnl=-0.00, balance=25696.80
[DEBUG] Step=357, action=1, return=0.3628, raw_pnl=362.76, actual_pnl=269.82, balance=25966.61
[DEBUG] Step=358, action=1, return=-0.0345, raw_pnl=-34.49, actual_pnl=-34.49, balance=25932.12
[DEBUG] Step=359, action=0, return=-0.4399, raw_pnl=-0.00, actual_pnl=-0.00, balance=25932.12
[DEBUG] Step=360, action=0, return=-0.0180, raw_pnl=-0.00, actual_pnl=-0.00, balance=25932.12
[DEBUG] Step=361, action=0, return=0.3411, raw_pnl=0.00, actual_pnl=0.00, balance=25932.12
[DEBUG] Step=362, action=1, return=0.3154, raw_pnl=315.37, actual_pnl=272.29, balance=26204.41
[DEBUG] Step=363, action=1, return=0.0976, raw_pnl=97.61, actual_pnl=97.61, balance=26302.01
[DEBUG] Step=364, action=0, return=-0.4211, raw_pnl=-0.00, actual_pnl=-0.00, balance=26302.01
[DEBUG] Step=365, action=1, return=0.3857, raw_pnl=385.70, actual_pnl=276.17, balance=26578.19
[DEBUG] Step=366, action=0, return=-0.1338, raw_pnl=-0.00, actual_pnl=-0.00, balance=26578.19
[DEBUG] Step=367, action=1, return=0.4266, raw_pnl=426.55, actual_pnl=279.07, balance=26857.26
[DEBUG] Step=368, action=1, return=-0.0649, raw_pnl=-64.87, actual_pnl=-64.87, balance=26792.38
[DEBUG] Step=369, action=1, return=-0.0021, raw_pnl=-2.06, actual_pnl=-2.06, balance=26790.32
[DEBUG] Step=370, action=0, return=-0.2011, raw_pnl=-0.00, actual_pnl=-0.00, balance=26790.32
[DEBUG] Step=371, action=0, return=-0.0367, raw_pnl=-0.00, actual_pnl=-0.00, balance=26790.32
[DEBUG] Step=372, action=0, return=-0.1000, raw_pnl=-0.00, actual_pnl=-0.00, balance=26790.32
[DEBUG] Step=373, action=0, return=-0.1704, raw_pnl=-0.00, actual_pnl=-0.00, balance=26790.32
[DEBUG] Step=374, action=1, return=0.7652, raw_pnl=765.21, actual_pnl=281.30, balance=27071.62
[DEBUG] Step=375, action=1, return=-0.0278, raw_pnl=-27.79, actual_pnl=-27.79, balance=27043.83
[DEBUG] Step=376, action=1, return=0.1030, raw_pnl=103.05, actual_pnl=103.05, balance=27146.88
[DEBUG] Step=377, action=1, return=-0.0015, raw_pnl=-1.54, actual_pnl=-1.54, balance=27145.34
[DEBUG] Step=378, action=0, return=-0.2210, raw_pnl=-0.00, actual_pnl=-0.00, balance=27145.34
[DEBUG] Step=379, action=1, return=0.1373, raw_pnl=137.30, actual_pnl=137.30, balance=27282.64
[DEBUG] Step=380, action=1, return=0.0994, raw_pnl=99.37, actual_pnl=99.37, balance=27382.00
[DEBUG] Step=381, action=1, return=-0.0489, raw_pnl=-48.91, actual_pnl=-48.91, balance=27333.09
[DEBUG] Step=382, action=0, return=-0.3256, raw_pnl=-0.00, actual_pnl=-0.00, balance=27333.09
[DEBUG] Step=383, action=0, return=0.1629, raw_pnl=0.00, actual_pnl=0.00, balance=27333.09
[DEBUG] Step=384, action=0, return=-0.2216, raw_pnl=-0.00, actual_pnl=-0.00, balance=27333.09
[DEBUG] Step=385, action=1, return=0.7305, raw_pnl=730.54, actual_pnl=287.00, balance=27620.09
[DEBUG] Step=386, action=1, return=-0.1780, raw_pnl=-178.03, actual_pnl=-135.34, balance=27484.75
[DEBUG] Step=387, action=0, return=-0.2351, raw_pnl=-0.00, actual_pnl=-0.00, balance=27484.75
[DEBUG] Step=388, action=1, return=0.3606, raw_pnl=360.61, actual_pnl=288.59, balance=27773.34
[DEBUG] Step=389, action=1, return=-0.0320, raw_pnl=-32.05, actual_pnl=-32.05, balance=27741.30
[DEBUG] Step=390, action=0, return=-0.1607, raw_pnl=-0.00, actual_pnl=-0.00, balance=27741.30
[DEBUG] Step=391, action=0, return=-0.1801, raw_pnl=-0.00, actual_pnl=-0.00, balance=27741.30
[DEBUG] Step=392, action=1, return=0.5011, raw_pnl=501.11, actual_pnl=291.28, balance=28032.58
[DEBUG] Step=393, action=1, return=-0.0905, raw_pnl=-90.49, actual_pnl=-90.49, balance=27942.09
[DEBUG] Step=394, action=1, return=0.1658, raw_pnl=165.76, actual_pnl=165.76, balance=28107.85
[DEBUG] Step=395, action=1, return=-0.1423, raw_pnl=-142.27, actual_pnl=-137.73, balance=27970.12
[DEBUG] Step=396, action=1, return=0.2184, raw_pnl=218.41, actual_pnl=218.41, balance=28188.53
[DEBUG] Step=397, action=1, return=-0.1621, raw_pnl=-162.12, actual_pnl=-138.12, balance=28050.41
[DEBUG] Step=398, action=1, return=0.0058, raw_pnl=5.82, actual_pnl=5.82, balance=28056.23
[DEBUG] Step=399, action=1, return=0.2023, raw_pnl=202.26, actual_pnl=202.26, balance=28258.49
[DEBUG] Step=400, action=0, return=-0.2521, raw_pnl=-0.00, actual_pnl=-0.00, balance=28258.49
[DEBUG] Step=401, action=0, return=-0.1920, raw_pnl=-0.00, actual_pnl=-0.00, balance=28258.49
[DEBUG] Step=402, action=0, return=-0.0928, raw_pnl=-0.00, actual_pnl=-0.00, balance=28258.49
[DEBUG] Step=403, action=1, return=0.7060, raw_pnl=706.03, actual_pnl=296.71, balance=28555.20
[DEBUG] Step=404, action=1, return=-0.0768, raw_pnl=-76.82, actual_pnl=-76.82, balance=28478.38
[DEBUG] Step=405, action=1, return=0.0517, raw_pnl=51.70, actual_pnl=51.70, balance=28530.08
[DEBUG] Step=406, action=0, return=-0.2882, raw_pnl=-0.00, actual_pnl=-0.00, balance=28530.08
[DEBUG] Step=407, action=0, return=-0.0631, raw_pnl=-0.00, actual_pnl=-0.00, balance=28530.08
[DEBUG] Step=408, action=0, return=-0.1072, raw_pnl=-0.00, actual_pnl=-0.00, balance=28530.08
[DEBUG] Step=409, action=0, return=0.3312, raw_pnl=0.00, actual_pnl=0.00, balance=28530.08
[DEBUG] Step=410, action=1, return=0.1772, raw_pnl=177.20, actual_pnl=177.20, balance=28707.29
[DEBUG] Step=411, action=1, return=-0.1243, raw_pnl=-124.33, actual_pnl=-124.33, balance=28582.96
[DEBUG] Step=412, action=1, return=0.0325, raw_pnl=32.49, actual_pnl=32.49, balance=28615.44
[DEBUG] Step=413, action=1, return=0.3247, raw_pnl=324.66, actual_pnl=300.46, balance=28915.91
[DEBUG] Step=414, action=0, return=-0.2919, raw_pnl=-0.00, actual_pnl=-0.00, balance=28915.91
[DEBUG] Step=415, action=1, return=0.1229, raw_pnl=122.92, actual_pnl=122.92, balance=29038.83
[DEBUG] Step=416, action=1, return=0.1781, raw_pnl=178.11, actual_pnl=178.11, balance=29216.95
[DEBUG] Step=417, action=0, return=-0.2170, raw_pnl=-0.00, actual_pnl=-0.00, balance=29216.95
[DEBUG] Step=418, action=1, return=0.1615, raw_pnl=161.50, actual_pnl=161.50, balance=29378.45
[DEBUG] Step=419, action=1, return=0.1481, raw_pnl=148.13, actual_pnl=148.13, balance=29526.58
[DEBUG] Step=420, action=1, return=0.0468, raw_pnl=46.80, actual_pnl=46.80, balance=29573.38
[DEBUG] Step=421, action=0, return=-0.4116, raw_pnl=-0.00, actual_pnl=-0.00, balance=29573.38
[DEBUG] Step=422, action=1, return=0.6796, raw_pnl=679.57, actual_pnl=310.52, balance=29883.90
[DEBUG] Step=423, action=0, return=-0.2255, raw_pnl=-0.00, actual_pnl=-0.00, balance=29883.90
[DEBUG] Step=424, action=0, return=-0.1567, raw_pnl=-0.00, actual_pnl=-0.00, balance=29883.90
[DEBUG] Step=425, action=0, return=0.1597, raw_pnl=0.00, actual_pnl=0.00, balance=29883.90
[DEBUG] Step=426, action=1, return=0.3570, raw_pnl=356.99, actual_pnl=313.78, balance=30197.68
[DEBUG] Step=427, action=0, return=-0.2462, raw_pnl=-0.00, actual_pnl=-0.00, balance=30197.68
[DEBUG] Step=428, action=0, return=-0.1098, raw_pnl=-0.00, actual_pnl=-0.00, balance=30197.68
[DEBUG] Step=429, action=1, return=0.2293, raw_pnl=229.27, actual_pnl=229.27, balance=30426.95
[DEBUG] Step=430, action=0, return=-0.2408, raw_pnl=-0.00, actual_pnl=-0.00, balance=30426.95
[DEBUG] Step=431, action=0, return=-0.1325, raw_pnl=-0.00, actual_pnl=-0.00, balance=30426.95
[DEBUG] Step=432, action=0, return=0.0493, raw_pnl=0.00, actual_pnl=0.00, balance=30426.95
[DEBUG] Step=433, action=0, return=-0.0007, raw_pnl=-0.00, actual_pnl=-0.00, balance=30426.95
[DEBUG] Step=434, action=0, return=0.0211, raw_pnl=0.00, actual_pnl=0.00, balance=30426.95
[DEBUG] Step=435, action=0, return=-0.0114, raw_pnl=-0.00, actual_pnl=-0.00, balance=30426.95
[DEBUG] Step=436, action=1, return=0.4408, raw_pnl=440.85, actual_pnl=319.48, balance=30746.43
[DEBUG] Step=437, action=0, return=-0.2797, raw_pnl=-0.00, actual_pnl=-0.00, balance=30746.43
[DEBUG] Step=438, action=1, return=0.1386, raw_pnl=138.58, actual_pnl=138.58, balance=30885.02
[DEBUG] Step=439, action=1, return=0.4096, raw_pnl=409.55, actual_pnl=324.29, balance=31209.31
[DEBUG] Step=440, action=1, return=-0.2229, raw_pnl=-222.92, actual_pnl=-152.93, balance=31056.38
[DEBUG] Step=441, action=1, return=0.1313, raw_pnl=131.34, actual_pnl=131.34, balance=31187.73
[DEBUG] Step=442, action=0, return=-0.2970, raw_pnl=-0.00, actual_pnl=-0.00, balance=31187.73
[DEBUG] Step=443, action=0, return=0.0170, raw_pnl=0.00, actual_pnl=0.00, balance=31187.73
[DEBUG] Step=444, action=0, return=-0.1270, raw_pnl=-0.00, actual_pnl=-0.00, balance=31187.73
[DEBUG] Step=445, action=0, return=0.1230, raw_pnl=0.00, actual_pnl=0.00, balance=31187.73
[DEBUG] Step=446, action=1, return=0.0938, raw_pnl=93.81, actual_pnl=93.81, balance=31281.54
[DEBUG] Step=447, action=0, return=-0.0794, raw_pnl=-0.00, actual_pnl=-0.00, balance=31281.54
[DEBUG] Step=448, action=0, return=-0.0750, raw_pnl=-0.00, actual_pnl=-0.00, balance=31281.54
[DEBUG] Step=449, action=0, return=0.0293, raw_pnl=0.00, actual_pnl=0.00, balance=31281.54
[DEBUG] Step=450, action=1, return=0.3035, raw_pnl=303.53, actual_pnl=303.53, balance=31585.06
[DEBUG] Step=451, action=0, return=-0.1742, raw_pnl=-0.00, actual_pnl=-0.00, balance=31585.06
[DEBUG] Step=452, action=1, return=0.1309, raw_pnl=130.92, actual_pnl=130.92, balance=31715.98
[DEBUG] Step=453, action=1, return=0.1020, raw_pnl=101.99, actual_pnl=101.99, balance=31817.98
[DEBUG] Step=454, action=1, return=0.1244, raw_pnl=124.37, actual_pnl=124.37, balance=31942.35
[DEBUG] Step=455, action=0, return=-0.3852, raw_pnl=-0.00, actual_pnl=-0.00, balance=31942.35
[DEBUG] Step=456, action=1, return=0.7313, raw_pnl=731.35, actual_pnl=335.39, balance=32277.74
[DEBUG] Step=457, action=1, return=-0.0953, raw_pnl=-95.31, actual_pnl=-95.31, balance=32182.43
[DEBUG] Step=458, action=0, return=-0.3355, raw_pnl=-0.00, actual_pnl=-0.00, balance=32182.43
[DEBUG] Step=459, action=1, return=0.7320, raw_pnl=731.97, actual_pnl=337.92, balance=32520.34
[DEBUG] Step=460, action=1, return=0.0252, raw_pnl=25.24, actual_pnl=25.24, balance=32545.59
[DEBUG] Step=461, action=0, return=-0.4476, raw_pnl=-0.00, actual_pnl=-0.00, balance=32545.59
[DEBUG] Step=462, action=0, return=0.2034, raw_pnl=0.00, actual_pnl=0.00, balance=32545.59
[DEBUG] Step=463, action=1, return=0.4145, raw_pnl=414.55, actual_pnl=341.73, balance=32887.31
[DEBUG] Step=464, action=1, return=-0.0321, raw_pnl=-32.08, actual_pnl=-32.08, balance=32855.23
[DEBUG] Step=465, action=0, return=-0.3225, raw_pnl=-0.00, actual_pnl=-0.00, balance=32855.23
[DEBUG] Step=466, action=0, return=0.0210, raw_pnl=0.00, actual_pnl=0.00, balance=32855.23
[DEBUG] Step=467, action=0, return=0.1332, raw_pnl=0.00, actual_pnl=0.00, balance=32855.23
[DEBUG] Step=468, action=1, return=0.0832, raw_pnl=83.22, actual_pnl=83.22, balance=32938.45
[DEBUG] Step=469, action=1, return=0.0901, raw_pnl=90.08, actual_pnl=90.08, balance=33028.54
[DEBUG] Step=470, action=0, return=-0.1541, raw_pnl=-0.00, actual_pnl=-0.00, balance=33028.54
[DEBUG] Step=471, action=1, return=0.0684, raw_pnl=68.39, actual_pnl=68.39, balance=33096.93
[DEBUG] Step=472, action=1, return=0.1948, raw_pnl=194.82, actual_pnl=194.82, balance=33291.75
[DEBUG] Step=473, action=0, return=-0.4068, raw_pnl=-0.00, actual_pnl=-0.00, balance=33291.75
[DEBUG] Step=474, action=0, return=0.2081, raw_pnl=0.00, actual_pnl=0.00, balance=33291.75
[DEBUG] Step=475, action=1, return=0.3680, raw_pnl=368.01, actual_pnl=349.56, balance=33641.32
[DEBUG] Step=476, action=1, return=0.1061, raw_pnl=106.14, actual_pnl=106.14, balance=33747.46
[DEBUG] Step=477, action=1, return=-0.2024, raw_pnl=-202.37, actual_pnl=-165.36, balance=33582.10
[DEBUG] Step=478, action=1, return=0.0135, raw_pnl=13.52, actual_pnl=13.52, balance=33595.61
[DEBUG] Step=479, action=0, return=-0.2774, raw_pnl=-0.00, actual_pnl=-0.00, balance=33595.61
[DEBUG] Step=480, action=1, return=0.3073, raw_pnl=307.31, actual_pnl=307.31, balance=33902.92
[DEBUG] Step=481, action=1, return=0.0589, raw_pnl=58.87, actual_pnl=58.87, balance=33961.79
[DEBUG] Step=482, action=0, return=-0.1893, raw_pnl=-0.00, actual_pnl=-0.00, balance=33961.79
[DEBUG] Step=483, action=0, return=0.0215, raw_pnl=0.00, actual_pnl=0.00, balance=33961.79
[DEBUG] Step=484, action=0, return=0.0851, raw_pnl=0.00, actual_pnl=0.00, balance=33961.79
[DEBUG] Step=485, action=0, return=-0.2594, raw_pnl=-0.00, actual_pnl=-0.00, balance=33961.79
[DEBUG] Step=486, action=0, return=0.2961, raw_pnl=0.00, actual_pnl=0.00, balance=33961.79
[DEBUG] Step=487, action=0, return=-0.0837, raw_pnl=-0.00, actual_pnl=-0.00, balance=33961.79
[DEBUG] Step=488, action=0, return=0.0958, raw_pnl=0.00, actual_pnl=0.00, balance=33961.79
[DEBUG] Step=489, action=0, return=-0.1565, raw_pnl=-0.00, actual_pnl=-0.00, balance=33961.79
[DEBUG] Step=490, action=1, return=0.6883, raw_pnl=688.33, actual_pnl=356.60, balance=34318.39
[DEBUG] Step=491, action=1, return=-0.1571, raw_pnl=-157.06, actual_pnl=-157.06, balance=34161.32
[DEBUG] Step=492, action=1, return=0.0537, raw_pnl=53.66, actual_pnl=53.66, balance=34214.98
[DEBUG] Step=493, action=1, return=0.0656, raw_pnl=65.55, actual_pnl=65.55, balance=34280.53
[DEBUG] Step=494, action=1, return=-0.1625, raw_pnl=-162.49, actual_pnl=-162.49, balance=34118.04
[DEBUG] Step=495, action=0, return=-0.2746, raw_pnl=-0.00, actual_pnl=-0.00, balance=34118.04
[DEBUG] Step=496, action=1, return=0.4142, raw_pnl=414.19, actual_pnl=358.24, balance=34476.28
[DEBUG] Step=497, action=1, return=0.0324, raw_pnl=32.36, actual_pnl=32.36, balance=34508.63
[DEBUG] Step=498, action=1, return=0.0999, raw_pnl=99.95, actual_pnl=99.95, balance=34608.58
[DEBUG] Step=499, action=0, return=-0.1798, raw_pnl=-0.00, actual_pnl=-0.00, balance=34608.58
[DEBUG] Step=500, action=0, return=-0.2124, raw_pnl=-0.00, actual_pnl=-0.00, balance=34608.58
[DEBUG] Step=501, action=0, return=0.1385, raw_pnl=0.00, actual_pnl=0.00, balance=34608.58
[DEBUG] Step=502, action=0, return=0.0618, raw_pnl=0.00, actual_pnl=0.00, balance=34608.58
[DEBUG] Step=503, action=1, return=0.2075, raw_pnl=207.50, actual_pnl=207.50, balance=34816.08
[DEBUG] Step=504, action=1, return=-0.0457, raw_pnl=-45.65, actual_pnl=-45.65, balance=34770.42
[DEBUG] Step=505, action=0, return=-0.1367, raw_pnl=-0.00, actual_pnl=-0.00, balance=34770.42
[DEBUG] Step=506, action=1, return=0.4649, raw_pnl=464.88, actual_pnl=365.09, balance=35135.51
[DEBUG] Step=507, action=1, return=-0.1917, raw_pnl=-191.66, actual_pnl=-172.16, balance=34963.35
[DEBUG] Step=508, action=0, return=-0.2295, raw_pnl=-0.00, actual_pnl=-0.00, balance=34963.35
[DEBUG] Step=509, action=0, return=-0.1095, raw_pnl=-0.00, actual_pnl=-0.00, balance=34963.35
[DEBUG] Step=510, action=0, return=0.0464, raw_pnl=0.00, actual_pnl=0.00, balance=34963.35
[DEBUG] Step=511, action=0, return=0.0808, raw_pnl=0.00, actual_pnl=0.00, balance=34963.35
[DEBUG] Step=512, action=0, return=-0.0684, raw_pnl=-0.00, actual_pnl=-0.00, balance=34963.35
[DEBUG] Step=513, action=0, return=0.0223, raw_pnl=0.00, actual_pnl=0.00, balance=34963.35
[DEBUG] Step=514, action=0, return=0.0830, raw_pnl=0.00, actual_pnl=0.00, balance=34963.35
[DEBUG] Step=515, action=0, return=-0.0869, raw_pnl=-0.00, actual_pnl=-0.00, balance=34963.35
[DEBUG] Step=516, action=1, return=0.6165, raw_pnl=616.51, actual_pnl=367.12, balance=35330.46
[DEBUG] Step=517, action=0, return=-0.4305, raw_pnl=-0.00, actual_pnl=-0.00, balance=35330.46
[DEBUG] Step=518, action=1, return=0.4113, raw_pnl=411.28, actual_pnl=370.97, balance=35701.43
[DEBUG] Step=519, action=1, return=-0.0749, raw_pnl=-74.85, actual_pnl=-74.85, balance=35626.58
[DEBUG] Step=520, action=1, return=0.4055, raw_pnl=405.55, actual_pnl=374.08, balance=36000.66
[DEBUG] Step=521, action=0, return=-0.4390, raw_pnl=-0.00, actual_pnl=-0.00, balance=36000.66
[DEBUG] Step=522, action=1, return=0.2570, raw_pnl=257.02, actual_pnl=257.02, balance=36257.68
[DEBUG] Step=523, action=1, return=0.4089, raw_pnl=408.92, actual_pnl=380.71, balance=36638.39
[DEBUG] Step=524, action=1, return=-0.0528, raw_pnl=-52.79, actual_pnl=-52.79, balance=36585.60
[DEBUG] Step=525, action=1, return=-0.0260, raw_pnl=-25.96, actual_pnl=-25.96, balance=36559.64
[DEBUG] Step=526, action=0, return=-0.3077, raw_pnl=-0.00, actual_pnl=-0.00, balance=36559.64
[DEBUG] Step=527, action=0, return=-0.0692, raw_pnl=-0.00, actual_pnl=-0.00, balance=36559.64
[DEBUG] Step=528, action=1, return=0.4251, raw_pnl=425.11, actual_pnl=383.88, balance=36943.51
[DEBUG] Step=529, action=1, return=0.1563, raw_pnl=156.25, actual_pnl=156.25, balance=37099.77
[DEBUG] Step=530, action=1, return=-0.1931, raw_pnl=-193.13, actual_pnl=-181.79, balance=36917.98
[DEBUG] Step=531, action=1, return=0.0095, raw_pnl=9.54, actual_pnl=9.54, balance=36927.52
[DEBUG] Step=532, action=0, return=-0.1856, raw_pnl=-0.00, actual_pnl=-0.00, balance=36927.52
[DEBUG] Step=533, action=1, return=0.3824, raw_pnl=382.44, actual_pnl=382.44, balance=37309.96
[DEBUG] Step=534, action=0, return=-0.3292, raw_pnl=-0.00, actual_pnl=-0.00, balance=37309.96
[DEBUG] Step=535, action=0, return=0.1151, raw_pnl=0.00, actual_pnl=0.00, balance=37309.96
[DEBUG] Step=536, action=0, return=0.0769, raw_pnl=0.00, actual_pnl=0.00, balance=37309.96
[DEBUG] Step=537, action=1, return=0.0576, raw_pnl=57.65, actual_pnl=57.65, balance=37367.60
[DEBUG] Step=538, action=0, return=-0.1759, raw_pnl=-0.00, actual_pnl=-0.00, balance=37367.60
[DEBUG] Step=539, action=0, return=-0.1027, raw_pnl=-0.00, actual_pnl=-0.00, balance=37367.60
[DEBUG] Step=540, action=1, return=0.4447, raw_pnl=444.71, actual_pnl=392.36, balance=37759.96
[DEBUG] Step=541, action=0, return=-0.1999, raw_pnl=-0.00, actual_pnl=-0.00, balance=37759.96
[DEBUG] Step=542, action=1, return=0.2271, raw_pnl=227.07, actual_pnl=227.07, balance=37987.03
[DEBUG] Step=543, action=0, return=-0.2700, raw_pnl=-0.00, actual_pnl=-0.00, balance=37987.03
[DEBUG] Step=544, action=1, return=0.2831, raw_pnl=283.08, actual_pnl=283.08, balance=38270.11
[DEBUG] Step=545, action=1, return=0.0347, raw_pnl=34.74, actual_pnl=34.74, balance=38304.85
[DEBUG] Step=546, action=0, return=-0.3137, raw_pnl=-0.00, actual_pnl=-0.00, balance=38304.85
[DEBUG] Step=547, action=1, return=0.2707, raw_pnl=270.75, actual_pnl=270.75, balance=38575.60
[DEBUG] Step=548, action=0, return=-0.1513, raw_pnl=-0.00, actual_pnl=-0.00, balance=38575.60
[DEBUG] Step=549, action=0, return=-0.0626, raw_pnl=-0.00, actual_pnl=-0.00, balance=38575.60
[DEBUG] Step=550, action=1, return=0.8714, raw_pnl=871.36, actual_pnl=405.04, balance=38980.64
[DEBUG] Step=551, action=1, return=-0.3355, raw_pnl=-335.49, actual_pnl=-191.01, balance=38789.64
[DEBUG] Step=552, action=1, return=0.3687, raw_pnl=368.68, actual_pnl=368.68, balance=39158.31
[DEBUG] Step=553, action=0, return=-0.3068, raw_pnl=-0.00, actual_pnl=-0.00, balance=39158.31
[DEBUG] Step=554, action=1, return=0.3402, raw_pnl=340.23, actual_pnl=340.23, balance=39498.54
[DEBUG] Step=555, action=1, return=0.0468, raw_pnl=46.82, actual_pnl=46.82, balance=39545.36
[DEBUG] Step=556, action=1, return=-0.0935, raw_pnl=-93.50, actual_pnl=-93.50, balance=39451.85
[DEBUG] Step=557, action=1, return=-0.0778, raw_pnl=-77.75, actual_pnl=-77.75, balance=39374.10
[DEBUG] Step=558, action=1, return=-0.0406, raw_pnl=-40.59, actual_pnl=-40.59, balance=39333.51
[DEBUG] Step=559, action=0, return=-0.0446, raw_pnl=-0.00, actual_pnl=-0.00, balance=39333.51
[DEBUG] Step=560, action=1, return=0.4305, raw_pnl=430.48, actual_pnl=413.00, balance=39746.51
[DEBUG] Step=561, action=1, return=-0.0513, raw_pnl=-51.26, actual_pnl=-51.26, balance=39695.25
[DEBUG] Step=562, action=1, return=0.0734, raw_pnl=73.42, actual_pnl=73.42, balance=39768.67
[DEBUG] Step=563, action=0, return=-0.4278, raw_pnl=-0.00, actual_pnl=-0.00, balance=39768.67
[DEBUG] Step=564, action=1, return=0.5395, raw_pnl=539.51, actual_pnl=417.57, balance=40186.24
[DEBUG] Step=565, action=1, return=0.1199, raw_pnl=119.87, actual_pnl=119.87, balance=40306.11
[DEBUG] Step=566, action=0, return=-0.3906, raw_pnl=-0.00, actual_pnl=-0.00, balance=40306.11
[DEBUG] Step=567, action=0, return=-0.0971, raw_pnl=-0.00, actual_pnl=-0.00, balance=40306.11
[DEBUG] Step=568, action=1, return=0.6326, raw_pnl=632.56, actual_pnl=423.21, balance=40729.32
[DEBUG] Step=569, action=1, return=-0.0957, raw_pnl=-95.71, actual_pnl=-95.71, balance=40633.61
[DEBUG] Step=570, action=1, return=0.1698, raw_pnl=169.81, actual_pnl=169.81, balance=40803.42
[DEBUG] Step=571, action=0, return=-0.3812, raw_pnl=-0.00, actual_pnl=-0.00, balance=40803.42
[DEBUG] Step=572, action=1, return=0.5751, raw_pnl=575.11, actual_pnl=428.44, balance=41231.85
[DEBUG] Step=573, action=0, return=-0.3307, raw_pnl=-0.00, actual_pnl=-0.00, balance=41231.85
[DEBUG] Step=574, action=0, return=-0.0316, raw_pnl=-0.00, actual_pnl=-0.00, balance=41231.85
[DEBUG] Step=575, action=0, return=0.0005, raw_pnl=0.00, actual_pnl=0.00, balance=41231.85
[DEBUG] Step=576, action=1, return=0.5586, raw_pnl=558.56, actual_pnl=432.93, balance=41664.79
[DEBUG] Step=577, action=1, return=-0.0823, raw_pnl=-82.32, actual_pnl=-82.32, balance=41582.47
[DEBUG] Step=578, action=1, return=-0.0854, raw_pnl=-85.35, actual_pnl=-85.35, balance=41497.11
[DEBUG] Step=579, action=0, return=-0.1078, raw_pnl=-0.00, actual_pnl=-0.00, balance=41497.11
[DEBUG] Step=580, action=1, return=0.3815, raw_pnl=381.48, actual_pnl=381.48, balance=41878.60
[DEBUG] Step=581, action=0, return=-0.2582, raw_pnl=-0.00, actual_pnl=-0.00, balance=41878.60
[DEBUG] Step=582, action=1, return=0.3046, raw_pnl=304.61, actual_pnl=304.61, balance=42183.21
[DEBUG] Step=583, action=0, return=-0.2078, raw_pnl=-0.00, actual_pnl=-0.00, balance=42183.21
[DEBUG] Step=584, action=0, return=-0.0432, raw_pnl=-0.00, actual_pnl=-0.00, balance=42183.21
[DEBUG] Step=585, action=1, return=0.0623, raw_pnl=62.26, actual_pnl=62.26, balance=42245.47
[DEBUG] Step=586, action=0, return=-0.1103, raw_pnl=-0.00, actual_pnl=-0.00, balance=42245.47
[DEBUG] Step=587, action=1, return=0.3429, raw_pnl=342.89, actual_pnl=342.89, balance=42588.36
[DEBUG] Step=588, action=1, return=-0.1401, raw_pnl=-140.13, actual_pnl=-140.13, balance=42448.24
[DEBUG] Step=589, action=0, return=-0.1800, raw_pnl=-0.00, actual_pnl=-0.00, balance=42448.24
[DEBUG] Step=590, action=1, return=0.5416, raw_pnl=541.60, actual_pnl=445.71, balance=42893.94
[DEBUG] Step=591, action=0, return=-0.2715, raw_pnl=-0.00, actual_pnl=-0.00, balance=42893.94
[DEBUG] Step=592, action=1, return=0.1154, raw_pnl=115.37, actual_pnl=115.37, balance=43009.31
[DEBUG] Step=593, action=1, return=0.2351, raw_pnl=235.12, actual_pnl=235.12, balance=43244.43
[DEBUG] Step=594, action=1, return=-0.1480, raw_pnl=-148.04, actual_pnl=-148.04, balance=43096.39
[DEBUG] Step=595, action=0, return=-0.3124, raw_pnl=-0.00, actual_pnl=-0.00, balance=43096.39
[DEBUG] Step=596, action=1, return=0.7368, raw_pnl=736.80, actual_pnl=452.51, balance=43548.90
[DEBUG] Step=597, action=1, return=-0.1609, raw_pnl=-160.90, actual_pnl=-160.90, balance=43388.00
[DEBUG] Step=598, action=0, return=-0.1799, raw_pnl=-0.00, actual_pnl=-0.00, balance=43388.00
[DEBUG] Step=599, action=0, return=-0.1466, raw_pnl=-0.00, actual_pnl=-0.00, balance=43388.00
[DEBUG] Step=600, action=1, return=0.5747, raw_pnl=574.71, actual_pnl=455.57, balance=43843.58
[DEBUG] Step=601, action=1, return=-0.0970, raw_pnl=-96.96, actual_pnl=-96.96, balance=43746.61
[DEBUG] Step=602, action=1, return=-0.0535, raw_pnl=-53.46, actual_pnl=-53.46, balance=43693.15
[DEBUG] Step=603, action=1, return=0.2350, raw_pnl=235.04, actual_pnl=235.04, balance=43928.20
[DEBUG] Step=604, action=1, return=-0.0556, raw_pnl=-55.60, actual_pnl=-55.60, balance=43872.60
[DEBUG] Step=605, action=0, return=-0.3561, raw_pnl=-0.00, actual_pnl=-0.00, balance=43872.60
[DEBUG] Step=606, action=0, return=0.1390, raw_pnl=0.00, actual_pnl=0.00, balance=43872.60
[DEBUG] Step=607, action=0, return=-0.0482, raw_pnl=-0.00, actual_pnl=-0.00, balance=43872.60
[DEBUG] Step=608, action=1, return=0.3968, raw_pnl=396.85, actual_pnl=396.85, balance=44269.45
[DEBUG] Step=609, action=0, return=-0.4074, raw_pnl=-0.00, actual_pnl=-0.00, balance=44269.45
[DEBUG] Step=610, action=1, return=0.5190, raw_pnl=518.96, actual_pnl=464.83, balance=44734.27
[DEBUG] Step=611, action=1, return=0.1227, raw_pnl=122.66, actual_pnl=122.66, balance=44856.94
[DEBUG] Step=612, action=1, return=0.0649, raw_pnl=64.86, actual_pnl=64.86, balance=44921.79
[DEBUG] Step=613, action=0, return=-0.2849, raw_pnl=-0.00, actual_pnl=-0.00, balance=44921.79
[DEBUG] Step=614, action=1, return=0.3570, raw_pnl=357.04, actual_pnl=357.04, balance=45278.83
[DEBUG] Step=615, action=0, return=-0.3902, raw_pnl=-0.00, actual_pnl=-0.00, balance=45278.83
[DEBUG] Step=616, action=1, return=0.6625, raw_pnl=662.52, actual_pnl=475.43, balance=45754.26
[DEBUG] Step=617, action=0, return=-0.3894, raw_pnl=-0.00, actual_pnl=-0.00, balance=45754.26
[DEBUG] Step=618, action=0, return=0.2393, raw_pnl=0.00, actual_pnl=0.00, balance=45754.26
[DEBUG] Step=619, action=1, return=0.2863, raw_pnl=286.27, actual_pnl=286.27, balance=46040.54
[DEBUG] Step=620, action=0, return=-0.3602, raw_pnl=-0.00, actual_pnl=-0.00, balance=46040.54
[DEBUG] Step=621, action=0, return=0.0690, raw_pnl=0.00, actual_pnl=0.00, balance=46040.54
[DEBUG] Step=622, action=1, return=0.4011, raw_pnl=401.06, actual_pnl=401.06, balance=46441.59
[DEBUG] Step=623, action=1, return=-0.0013, raw_pnl=-1.29, actual_pnl=-1.29, balance=46440.31
[DEBUG] Step=624, action=1, return=-0.0459, raw_pnl=-45.86, actual_pnl=-45.86, balance=46394.44
[DEBUG] Step=625, action=1, return=0.0322, raw_pnl=32.17, actual_pnl=32.17, balance=46426.62
[DEBUG] Step=626, action=1, return=-0.0893, raw_pnl=-89.27, actual_pnl=-89.27, balance=46337.34
[DEBUG] Step=627, action=0, return=-0.1886, raw_pnl=-0.00, actual_pnl=-0.00, balance=46337.34
[DEBUG] Step=628, action=0, return=0.0750, raw_pnl=0.00, actual_pnl=0.00, balance=46337.34
[DEBUG] Step=629, action=0, return=-0.1219, raw_pnl=-0.00, actual_pnl=-0.00, balance=46337.34
[DEBUG] Step=630, action=1, return=0.6151, raw_pnl=615.14, actual_pnl=486.54, balance=46823.89
[DEBUG] Step=631, action=1, return=-0.1703, raw_pnl=-170.33, actual_pnl=-170.33, balance=46653.56
[DEBUG] Step=632, action=0, return=-0.1153, raw_pnl=-0.00, actual_pnl=-0.00, balance=46653.56
[DEBUG] Step=633, action=1, return=0.0437, raw_pnl=43.66, actual_pnl=43.66, balance=46697.21
[DEBUG] Step=634, action=1, return=0.3319, raw_pnl=331.93, actual_pnl=331.93, balance=47029.14
[DEBUG] Step=635, action=0, return=-0.4077, raw_pnl=-0.00, actual_pnl=-0.00, balance=47029.14
[DEBUG] Step=636, action=1, return=0.3753, raw_pnl=375.32, actual_pnl=375.32, balance=47404.46
[DEBUG] Step=637, action=1, return=-0.0506, raw_pnl=-50.65, actual_pnl=-50.65, balance=47353.81
[DEBUG] Step=638, action=1, return=0.0701, raw_pnl=70.10, actual_pnl=70.10, balance=47423.92
[DEBUG] Step=639, action=0, return=-0.3682, raw_pnl=-0.00, actual_pnl=-0.00, balance=47423.92
[DEBUG] Step=640, action=1, return=0.8388, raw_pnl=838.82, actual_pnl=497.95, balance=47921.87
[DEBUG] Step=641, action=1, return=0.0320, raw_pnl=32.05, actual_pnl=32.05, balance=47953.91
[DEBUG] Step=642, action=1, return=-0.1899, raw_pnl=-189.94, actual_pnl=-189.94, balance=47763.97
[DEBUG] Step=643, action=1, return=0.0840, raw_pnl=84.03, actual_pnl=84.03, balance=47848.00
[DEBUG] Step=644, action=1, return=0.1331, raw_pnl=133.11, actual_pnl=133.11, balance=47981.12
[DEBUG] Step=645, action=1, return=-0.1120, raw_pnl=-111.97, actual_pnl=-111.97, balance=47869.15
[DEBUG] Step=646, action=0, return=-0.3249, raw_pnl=-0.00, actual_pnl=-0.00, balance=47869.15
[DEBUG] Step=647, action=1, return=0.3677, raw_pnl=367.67, actual_pnl=367.67, balance=48236.81
[DEBUG] Step=648, action=1, return=0.0193, raw_pnl=19.30, actual_pnl=19.30, balance=48256.12
[DEBUG] Step=649, action=0, return=-0.1136, raw_pnl=-0.00, actual_pnl=-0.00, balance=48256.12
[DEBUG] Step=650, action=1, return=0.2193, raw_pnl=219.30, actual_pnl=219.30, balance=48475.42
[DEBUG] Step=651, action=1, return=0.1140, raw_pnl=113.98, actual_pnl=113.98, balance=48589.40
[DEBUG] Step=652, action=1, return=-0.0045, raw_pnl=-4.55, actual_pnl=-4.55, balance=48584.85
[DEBUG] Step=653, action=0, return=-0.2465, raw_pnl=-0.00, actual_pnl=-0.00, balance=48584.85
[DEBUG] Step=654, action=0, return=-0.2327, raw_pnl=-0.00, actual_pnl=-0.00, balance=48584.85
[DEBUG] Step=655, action=1, return=0.7829, raw_pnl=782.94, actual_pnl=510.14, balance=49094.99
[DEBUG] Step=656, action=1, return=-0.0735, raw_pnl=-73.53, actual_pnl=-73.53, balance=49021.46
[DEBUG] Step=657, action=0, return=-0.3884, raw_pnl=-0.00, actual_pnl=-0.00, balance=49021.46
[DEBUG] Step=658, action=1, return=0.7079, raw_pnl=707.93, actual_pnl=514.73, balance=49536.19
[DEBUG] Step=659, action=1, return=-0.0265, raw_pnl=-26.52, actual_pnl=-26.52, balance=49509.67
[DEBUG] Step=660, action=0, return=-0.1877, raw_pnl=-0.00, actual_pnl=-0.00, balance=49509.67
[DEBUG] Step=661, action=1, return=0.0477, raw_pnl=47.69, actual_pnl=47.69, balance=49557.36
[DEBUG] Step=662, action=0, return=-0.1208, raw_pnl=-0.00, actual_pnl=-0.00, balance=49557.36
[DEBUG] Step=663, action=0, return=-0.2461, raw_pnl=-0.00, actual_pnl=-0.00, balance=49557.36
[DEBUG] Step=664, action=0, return=0.2659, raw_pnl=0.00, actual_pnl=0.00, balance=49557.36
[DEBUG] Step=665, action=1, return=0.3503, raw_pnl=350.25, actual_pnl=350.25, balance=49907.61
[DEBUG] Step=666, action=0, return=-0.4428, raw_pnl=-0.00, actual_pnl=-0.00, balance=49907.61
[DEBUG] Step=667, action=0, return=0.3274, raw_pnl=0.00, actual_pnl=0.00, balance=49907.61
[DEBUG] Step=668, action=0, return=0.0485, raw_pnl=0.00, actual_pnl=0.00, balance=49907.61
[DEBUG] Step=669, action=1, return=0.0996, raw_pnl=99.58, actual_pnl=99.58, balance=50007.19
[DEBUG] Step=670, action=1, return=0.2488, raw_pnl=248.77, actual_pnl=248.77, balance=50255.96
[DEBUG] Step=671, action=0, return=-0.2987, raw_pnl=-0.00, actual_pnl=-0.00, balance=50255.96
[DEBUG] Step=672, action=0, return=0.0005, raw_pnl=0.00, actual_pnl=0.00, balance=50255.96
[DEBUG] Step=673, action=1, return=0.2899, raw_pnl=289.95, actual_pnl=289.95, balance=50545.91
[DEBUG] Step=674, action=1, return=-0.1642, raw_pnl=-164.19, actual_pnl=-164.19, balance=50381.72
[DEBUG] Step=675, action=0, return=-0.1567, raw_pnl=-0.00, actual_pnl=-0.00, balance=50381.72
[DEBUG] Step=676, action=1, return=0.1860, raw_pnl=186.05, actual_pnl=186.05, balance=50567.77
[DEBUG] Step=677, action=0, return=-0.2145, raw_pnl=-0.00, actual_pnl=-0.00, balance=50567.77
[DEBUG] Step=678, action=0, return=0.0311, raw_pnl=0.00, actual_pnl=0.00, balance=50567.77
[DEBUG] Step=679, action=1, return=0.2737, raw_pnl=273.70, actual_pnl=273.70, balance=50841.47
[DEBUG] Step=680, action=1, return=-0.0530, raw_pnl=-53.02, actual_pnl=-53.02, balance=50788.45
[DEBUG] Step=681, action=1, return=0.3495, raw_pnl=349.50, actual_pnl=349.50, balance=51137.95
[DEBUG] Step=682, action=0, return=-0.2885, raw_pnl=-0.00, actual_pnl=-0.00, balance=51137.95
[DEBUG] Step=683, action=1, return=0.1602, raw_pnl=160.16, actual_pnl=160.16, balance=51298.11
[DEBUG] Step=684, action=1, return=0.0327, raw_pnl=32.69, actual_pnl=32.69, balance=51330.80
[DEBUG] Step=685, action=0, return=-0.3793, raw_pnl=-0.00, actual_pnl=-0.00, balance=51330.80
[DEBUG] Step=686, action=1, return=0.6420, raw_pnl=642.04, actual_pnl=538.97, balance=51869.78
[DEBUG] Step=687, action=0, return=-0.2918, raw_pnl=-0.00, actual_pnl=-0.00, balance=51869.78
[DEBUG] Step=688, action=1, return=0.6647, raw_pnl=664.69, actual_pnl=544.63, balance=52414.41
[DEBUG] Step=689, action=0, return=-0.4143, raw_pnl=-0.00, actual_pnl=-0.00, balance=52414.41
[DEBUG] Step=690, action=1, return=0.2315, raw_pnl=231.54, actual_pnl=231.54, balance=52645.95
[DEBUG] Step=691, action=0, return=-0.2328, raw_pnl=-0.00, actual_pnl=-0.00, balance=52645.95
[DEBUG] Step=692, action=1, return=0.8398, raw_pnl=839.84, actual_pnl=552.78, balance=53198.73
[DEBUG] Step=693, action=1, return=-0.2477, raw_pnl=-247.73, actual_pnl=-247.73, balance=52951.00
[DEBUG] Step=694, action=1, return=0.0620, raw_pnl=62.04, actual_pnl=62.04, balance=53013.04
[DEBUG] Step=695, action=0, return=-0.3311, raw_pnl=-0.00, actual_pnl=-0.00, balance=53013.04
[DEBUG] Step=696, action=1, return=0.6400, raw_pnl=639.96, actual_pnl=556.64, balance=53569.68
[DEBUG] Step=697, action=0, return=-0.3086, raw_pnl=-0.00, actual_pnl=-0.00, balance=53569.68
[DEBUG] Step=698, action=1, return=0.5688, raw_pnl=568.76, actual_pnl=562.48, balance=54132.16
[DEBUG] Step=699, action=0, return=-0.3651, raw_pnl=-0.00, actual_pnl=-0.00, balance=54132.16
[DEBUG] Step=700, action=0, return=-0.0120, raw_pnl=-0.00, actual_pnl=-0.00, balance=54132.16
[DEBUG] Step=701, action=0, return=-0.1295, raw_pnl=-0.00, actual_pnl=-0.00, balance=54132.16
[DEBUG] Step=702, action=1, return=0.4202, raw_pnl=420.16, actual_pnl=420.16, balance=54552.32
[DEBUG] Step=703, action=1, return=0.0630, raw_pnl=63.02, actual_pnl=63.02, balance=54615.34
[DEBUG] Step=704, action=0, return=-0.3190, raw_pnl=-0.00, actual_pnl=-0.00, balance=54615.34
[DEBUG] Step=705, action=1, return=0.6661, raw_pnl=666.05, actual_pnl=573.46, balance=55188.80
[DEBUG] Step=706, action=1, return=-0.1815, raw_pnl=-181.49, actual_pnl=-181.49, balance=55007.31
[DEBUG] Step=707, action=1, return=0.0489, raw_pnl=48.92, actual_pnl=48.92, balance=55056.24
[DEBUG] Step=708, action=1, return=-0.0549, raw_pnl=-54.86, actual_pnl=-54.86, balance=55001.38
[DEBUG] Step=709, action=1, return=-0.0278, raw_pnl=-27.76, actual_pnl=-27.76, balance=54973.62
[DEBUG] Step=710, action=1, return=0.1134, raw_pnl=113.42, actual_pnl=113.42, balance=55087.04
[DEBUG] Step=711, action=0, return=-0.2593, raw_pnl=-0.00, actual_pnl=-0.00, balance=55087.04
[DEBUG] Step=712, action=0, return=0.0231, raw_pnl=0.00, actual_pnl=0.00, balance=55087.04
[DEBUG] Step=713, action=1, return=0.5752, raw_pnl=575.21, actual_pnl=575.21, balance=55662.25
[DEBUG] Step=714, action=1, return=0.0453, raw_pnl=45.30, actual_pnl=45.30, balance=55707.54
[DEBUG] Step=715, action=0, return=-0.2943, raw_pnl=-0.00, actual_pnl=-0.00, balance=55707.54
[DEBUG] Step=716, action=0, return=-0.0747, raw_pnl=-0.00, actual_pnl=-0.00, balance=55707.54
[DEBUG] Step=717, action=1, return=0.2937, raw_pnl=293.73, actual_pnl=293.73, balance=56001.27
[DEBUG] Step=718, action=0, return=-0.1431, raw_pnl=-0.00, actual_pnl=-0.00, balance=56001.27
[DEBUG] Step=719, action=0, return=-0.2721, raw_pnl=-0.00, actual_pnl=-0.00, balance=56001.27
[DEBUG] Step=720, action=0, return=0.1275, raw_pnl=0.00, actual_pnl=0.00, balance=56001.27
[DEBUG] Step=721, action=1, return=0.4842, raw_pnl=484.21, actual_pnl=484.21, balance=56485.48
[DEBUG] Step=722, action=1, return=-0.0332, raw_pnl=-33.25, actual_pnl=-33.25, balance=56452.24
[DEBUG] Step=723, action=0, return=-0.3809, raw_pnl=-0.00, actual_pnl=-0.00, balance=56452.24
[DEBUG] Step=724, action=0, return=0.1897, raw_pnl=0.00, actual_pnl=0.00, balance=56452.24
[DEBUG] Step=725, action=0, return=0.0074, raw_pnl=0.00, actual_pnl=0.00, balance=56452.24
[DEBUG] Step=726, action=1, return=0.3581, raw_pnl=358.08, actual_pnl=358.08, balance=56810.31
[DEBUG] Step=727, action=0, return=-0.3901, raw_pnl=-0.00, actual_pnl=-0.00, balance=56810.31
[DEBUG] Step=728, action=0, return=0.0828, raw_pnl=0.00, actual_pnl=0.00, balance=56810.31
[DEBUG] Step=729, action=1, return=0.6302, raw_pnl=630.20, actual_pnl=596.51, balance=57406.82
[DEBUG] Step=730, action=0, return=-0.3452, raw_pnl=-0.00, actual_pnl=-0.00, balance=57406.82
[DEBUG] Step=731, action=1, return=0.4024, raw_pnl=402.36, actual_pnl=402.36, balance=57809.18
[DEBUG] Step=732, action=0, return=-0.2508, raw_pnl=-0.00, actual_pnl=-0.00, balance=57809.18
[DEBUG] Step=733, action=0, return=-0.1121, raw_pnl=-0.00, actual_pnl=-0.00, balance=57809.18
[DEBUG] Step=734, action=0, return=0.1307, raw_pnl=0.00, actual_pnl=0.00, balance=57809.18
[DEBUG] Step=735, action=1, return=0.3854, raw_pnl=385.38, actual_pnl=385.38, balance=58194.56
[DEBUG] Step=736, action=1, return=0.0775, raw_pnl=77.47, actual_pnl=77.47, balance=58272.04
[DEBUG] Step=737, action=1, return=-0.0137, raw_pnl=-13.73, actual_pnl=-13.73, balance=58258.31
[DEBUG] Step=738, action=1, return=-0.2366, raw_pnl=-236.60, actual_pnl=-236.60, balance=58021.70
[DEBUG] Step=739, action=1, return=0.1939, raw_pnl=193.89, actual_pnl=193.89, balance=58215.60
[DEBUG] Step=740, action=0, return=-0.2776, raw_pnl=-0.00, actual_pnl=-0.00, balance=58215.60
[DEBUG] Step=741, action=0, return=0.0732, raw_pnl=0.00, actual_pnl=0.00, balance=58215.60
[DEBUG] Step=742, action=1, return=0.4664, raw_pnl=466.45, actual_pnl=466.45, balance=58682.05
[DEBUG] Step=743, action=0, return=-0.4658, raw_pnl=-0.00, actual_pnl=-0.00, balance=58682.05
[DEBUG] Step=744, action=0, return=0.0716, raw_pnl=0.00, actual_pnl=0.00, balance=58682.05
[DEBUG] Step=745, action=0, return=0.1127, raw_pnl=0.00, actual_pnl=0.00, balance=58682.05
[DEBUG] Step=746, action=0, return=-0.1501, raw_pnl=-0.00, actual_pnl=-0.00, balance=58682.05
[DEBUG] Step=747, action=0, return=0.1509, raw_pnl=0.00, actual_pnl=0.00, balance=58682.05
[DEBUG] Step=748, action=1, return=0.3399, raw_pnl=339.93, actual_pnl=339.93, balance=59021.98
[DEBUG] Step=749, action=1, return=-0.1021, raw_pnl=-102.09, actual_pnl=-102.09, balance=58919.88
[DEBUG] Step=750, action=1, return=0.3315, raw_pnl=331.53, actual_pnl=331.53, balance=59251.42
[DEBUG] Step=751, action=1, return=-0.0397, raw_pnl=-39.75, actual_pnl=-39.75, balance=59211.67
[DEBUG] Step=752, action=0, return=-0.2617, raw_pnl=-0.00, actual_pnl=-0.00, balance=59211.67
[DEBUG] Step=753, action=0, return=-0.0614, raw_pnl=-0.00, actual_pnl=-0.00, balance=59211.67
[DEBUG] Step=754, action=1, return=0.0955, raw_pnl=95.50, actual_pnl=95.50, balance=59307.16
[DEBUG] Step=755, action=1, return=0.1526, raw_pnl=152.64, actual_pnl=152.64, balance=59459.81
[DEBUG] Step=756, action=0, return=-0.2026, raw_pnl=-0.00, actual_pnl=-0.00, balance=59459.81
[DEBUG] Step=757, action=1, return=0.2808, raw_pnl=280.81, actual_pnl=280.81, balance=59740.62
[DEBUG] Step=758, action=1, return=-0.1322, raw_pnl=-132.22, actual_pnl=-132.22, balance=59608.40
[DEBUG] Step=759, action=1, return=0.1012, raw_pnl=101.20, actual_pnl=101.20, balance=59709.60
[DEBUG] Step=760, action=1, return=-0.0747, raw_pnl=-74.69, actual_pnl=-74.69, balance=59634.92
[DEBUG] Step=761, action=0, return=-0.0986, raw_pnl=-0.00, actual_pnl=-0.00, balance=59634.92
[DEBUG] Step=762, action=1, return=0.5052, raw_pnl=505.22, actual_pnl=505.22, balance=60140.13
[DEBUG] Step=763, action=1, return=-0.0949, raw_pnl=-94.87, actual_pnl=-94.87, balance=60045.27
[DEBUG] Step=764, action=0, return=-0.3535, raw_pnl=-0.00, actual_pnl=-0.00, balance=60045.27
[DEBUG] Step=765, action=1, return=0.6388, raw_pnl=638.84, actual_pnl=630.48, balance=60675.74
[DEBUG] Step=766, action=1, return=-0.2039, raw_pnl=-203.93, actual_pnl=-203.93, balance=60471.81
[DEBUG] Step=767, action=1, return=0.2737, raw_pnl=273.71, actual_pnl=273.71, balance=60745.52
[DEBUG] Step=768, action=1, return=-0.0500, raw_pnl=-49.98, actual_pnl=-49.98, balance=60695.53
[DEBUG] Step=769, action=0, return=-0.2082, raw_pnl=-0.00, actual_pnl=-0.00, balance=60695.53
[DEBUG] Step=770, action=0, return=-0.2826, raw_pnl=-0.00, actual_pnl=-0.00, balance=60695.53
[DEBUG] Step=771, action=0, return=0.2408, raw_pnl=0.00, actual_pnl=0.00, balance=60695.53
[DEBUG] Step=772, action=1, return=0.2152, raw_pnl=215.15, actual_pnl=215.15, balance=60910.68
[DEBUG] Step=773, action=1, return=0.0596, raw_pnl=59.58, actual_pnl=59.58, balance=60970.26
[DEBUG] Step=774, action=0, return=-0.2299, raw_pnl=-0.00, actual_pnl=-0.00, balance=60970.26
[DEBUG] Step=775, action=0, return=-0.0942, raw_pnl=-0.00, actual_pnl=-0.00, balance=60970.26
[DEBUG] Step=776, action=1, return=0.6105, raw_pnl=610.50, actual_pnl=610.50, balance=61580.76
[DEBUG] Step=777, action=1, return=0.0815, raw_pnl=81.46, actual_pnl=81.46, balance=61662.22
[DEBUG] Step=778, action=1, return=-0.2312, raw_pnl=-231.16, actual_pnl=-231.16, balance=61431.06
[DEBUG] Step=779, action=0, return=-0.2320, raw_pnl=-0.00, actual_pnl=-0.00, balance=61431.06
[DEBUG] Step=780, action=0, return=0.0859, raw_pnl=0.00, actual_pnl=0.00, balance=61431.06
[DEBUG] Step=781, action=0, return=-0.1996, raw_pnl=-0.00, actual_pnl=-0.00, balance=61431.06
[DEBUG] Step=782, action=1, return=0.8797, raw_pnl=879.73, actual_pnl=645.03, balance=62076.08
[DEBUG] Step=783, action=0, return=-0.4161, raw_pnl=-0.00, actual_pnl=-0.00, balance=62076.08
[DEBUG] Step=784, action=1, return=0.4104, raw_pnl=410.44, actual_pnl=410.44, balance=62486.52
[DEBUG] Step=785, action=0, return=-0.1919, raw_pnl=-0.00, actual_pnl=-0.00, balance=62486.52
[DEBUG] Step=786, action=1, return=0.2199, raw_pnl=219.87, actual_pnl=219.87, balance=62706.39
[DEBUG] Step=787, action=1, return=0.0626, raw_pnl=62.57, actual_pnl=62.57, balance=62768.96
[DEBUG] Step=788, action=1, return=0.1080, raw_pnl=107.98, actual_pnl=107.98, balance=62876.94
[DEBUG] Step=789, action=0, return=-0.3407, raw_pnl=-0.00, actual_pnl=-0.00, balance=62876.94
[DEBUG] Step=790, action=0, return=-0.1620, raw_pnl=-0.00, actual_pnl=-0.00, balance=62876.94
[DEBUG] Step=791, action=0, return=0.1245, raw_pnl=0.00, actual_pnl=0.00, balance=62876.94
[DEBUG] Step=792, action=1, return=0.6712, raw_pnl=671.25, actual_pnl=660.21, balance=63537.14
[DEBUG] Step=793, action=1, return=-0.0138, raw_pnl=-13.75, actual_pnl=-13.75, balance=63523.39
[DEBUG] Step=794, action=1, return=-0.1475, raw_pnl=-147.54, actual_pnl=-147.54, balance=63375.85
[DEBUG] Step=795, action=1, return=0.0019, raw_pnl=1.94, actual_pnl=1.94, balance=63377.79
[DEBUG] Step=796, action=1, return=0.0403, raw_pnl=40.31, actual_pnl=40.31, balance=63418.11
[DEBUG] Step=797, action=0, return=-0.2941, raw_pnl=-0.00, actual_pnl=-0.00, balance=63418.11
[DEBUG] Step=798, action=1, return=0.6288, raw_pnl=628.77, actual_pnl=628.77, balance=64046.88
[DEBUG] Step=799, action=0, return=-0.2589, raw_pnl=-0.00, actual_pnl=-0.00, balance=64046.88
[DEBUG] Step=800, action=0, return=-0.0251, raw_pnl=-0.00, actual_pnl=-0.00, balance=64046.88
[DEBUG] Step=801, action=1, return=0.0982, raw_pnl=98.17, actual_pnl=98.17, balance=64145.05
[DEBUG] Step=802, action=0, return=-0.3107, raw_pnl=-0.00, actual_pnl=-0.00, balance=64145.05
[DEBUG] Step=803, action=0, return=0.1140, raw_pnl=0.00, actual_pnl=0.00, balance=64145.05
[DEBUG] Step=804, action=1, return=0.4902, raw_pnl=490.23, actual_pnl=490.23, balance=64635.28
[DEBUG] Step=805, action=0, return=-0.3770, raw_pnl=-0.00, actual_pnl=-0.00, balance=64635.28
[DEBUG] Step=806, action=1, return=0.4806, raw_pnl=480.56, actual_pnl=480.56, balance=65115.84
[DEBUG] Step=807, action=0, return=-0.2232, raw_pnl=-0.00, actual_pnl=-0.00, balance=65115.84
[DEBUG] Step=808, action=1, return=0.1156, raw_pnl=115.59, actual_pnl=115.59, balance=65231.43
[DEBUG] Step=809, action=0, return=-0.0724, raw_pnl=-0.00, actual_pnl=-0.00, balance=65231.43
[DEBUG] Step=810, action=1, return=0.0520, raw_pnl=51.97, actual_pnl=51.97, balance=65283.40
[DEBUG] Step=811, action=1, return=0.2680, raw_pnl=268.04, actual_pnl=268.04, balance=65551.44
[DEBUG] Step=812, action=0, return=-0.2454, raw_pnl=-0.00, actual_pnl=-0.00, balance=65551.44
[DEBUG] Step=813, action=1, return=0.2076, raw_pnl=207.60, actual_pnl=207.60, balance=65759.04
[DEBUG] Step=814, action=1, return=-0.0577, raw_pnl=-57.68, actual_pnl=-57.68, balance=65701.36
[DEBUG] Step=815, action=1, return=0.1271, raw_pnl=127.11, actual_pnl=127.11, balance=65828.47
[DEBUG] Step=816, action=1, return=0.1642, raw_pnl=164.19, actual_pnl=164.19, balance=65992.66
[DEBUG] Step=817, action=1, return=-0.1055, raw_pnl=-105.46, actual_pnl=-105.46, balance=65887.20
[DEBUG] Step=818, action=0, return=-0.2988, raw_pnl=-0.00, actual_pnl=-0.00, balance=65887.20
[DEBUG] Step=819, action=0, return=-0.1512, raw_pnl=-0.00, actual_pnl=-0.00, balance=65887.20
[DEBUG] Step=820, action=0, return=0.2241, raw_pnl=0.00, actual_pnl=0.00, balance=65887.20
[DEBUG] Step=821, action=1, return=0.2637, raw_pnl=263.66, actual_pnl=263.66, balance=66150.87
[DEBUG] Step=822, action=0, return=-0.3408, raw_pnl=-0.00, actual_pnl=-0.00, balance=66150.87
[DEBUG] Step=823, action=1, return=0.4232, raw_pnl=423.18, actual_pnl=423.18, balance=66574.04
[DEBUG] Step=824, action=1, return=0.0671, raw_pnl=67.15, actual_pnl=67.15, balance=66641.19
[DEBUG] Step=825, action=0, return=-0.1644, raw_pnl=-0.00, actual_pnl=-0.00, balance=66641.19
[DEBUG] Step=826, action=1, return=0.3273, raw_pnl=327.28, actual_pnl=327.28, balance=66968.47
[DEBUG] Step=827, action=0, return=-0.3751, raw_pnl=-0.00, actual_pnl=-0.00, balance=66968.47
[DEBUG] Step=828, action=0, return=-0.0284, raw_pnl=-0.00, actual_pnl=-0.00, balance=66968.47
[DEBUG] Step=829, action=1, return=0.6074, raw_pnl=607.41, actual_pnl=607.41, balance=67575.88
[DEBUG] Step=830, action=1, return=-0.1346, raw_pnl=-134.65, actual_pnl=-134.65, balance=67441.23
[DEBUG] Step=831, action=1, return=0.1290, raw_pnl=129.00, actual_pnl=129.00, balance=67570.23
[DEBUG] Step=832, action=1, return=-0.1502, raw_pnl=-150.19, actual_pnl=-150.19, balance=67420.04
[DEBUG] Step=833, action=0, return=-0.1313, raw_pnl=-0.00, actual_pnl=-0.00, balance=67420.04
[DEBUG] Step=834, action=1, return=0.4595, raw_pnl=459.48, actual_pnl=459.48, balance=67879.52
[DEBUG] Step=835, action=1, return=-0.0108, raw_pnl=-10.82, actual_pnl=-10.82, balance=67868.70
[DEBUG] Step=836, action=1, return=-0.0582, raw_pnl=-58.20, actual_pnl=-58.20, balance=67810.50
[DEBUG] Step=837, action=0, return=-0.2493, raw_pnl=-0.00, actual_pnl=-0.00, balance=67810.50
[DEBUG] Step=838, action=1, return=0.2500, raw_pnl=250.04, actual_pnl=250.04, balance=68060.54
[DEBUG] Step=839, action=0, return=-0.1442, raw_pnl=-0.00, actual_pnl=-0.00, balance=68060.54
[DEBUG] Step=840, action=0, return=-0.1979, raw_pnl=-0.00, actual_pnl=-0.00, balance=68060.54
[DEBUG] Step=841, action=1, return=0.7565, raw_pnl=756.45, actual_pnl=714.64, balance=68775.18
[DEBUG] Step=842, action=0, return=-0.4071, raw_pnl=-0.00, actual_pnl=-0.00, balance=68775.18
[DEBUG] Step=843, action=1, return=0.7155, raw_pnl=715.52, actual_pnl=715.52, balance=69490.70
[DEBUG] Step=844, action=0, return=-0.2585, raw_pnl=-0.00, actual_pnl=-0.00, balance=69490.70

Risk-Managed Ensemble Final Balance = 69490.70, Profit = 59490.70
