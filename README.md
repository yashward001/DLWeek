# StraddleAI: AI-Powered Options Trading Strategy

StraddleAI is an AI-powered trading strategy that implements a **Long Straddle Options Strategy** based on market volatility signals. It utilizes **machine learning models** to optimize trade execution and risk management.

## Features

- **Automated options trading** based on market volatility analysis.
- **Reinforcement Learning (RL) based strategy optimization**.
- **Backtesting and simulation support** to validate trading performance.
- **Risk management mechanisms** for better drawdown control.

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
| Initial Balance   | $100,00 |
| Final Balance     | $69,490.70 |
| Time | 3 years |
| Rate | 90.38% |

## Contribution

We welcome contributions! Follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your fork and submit a PR (`git push origin feature-branch`).

