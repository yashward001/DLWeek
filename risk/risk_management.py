# risk_management.py
import numpy as np

def get_risk_profile(profile):
    """
    Returns risk management parameters based on the selected risk profile.

    Parameters:
        profile (str): "high", "medium", or "low".

    Returns:
        dict: Risk parameters containing:
              - position_size_pct: Percentage of balance to risk per trade.
              - stop_loss_pct: Maximum loss percentage per trade.
              - take_profit_pct: Target profit percentage per trade.
              - max_drawdown_pct: Maximum allowed drawdown before risk adjustment.
              - trailing_stop_pct: Trailing stop percentage.
    """
    risk_profiles = {
        "high": {
            "position_size_pct": 0.15,
            "stop_loss_pct": 0.15,
            "take_profit_pct": 0.30,
            "max_drawdown_pct": 0.40,
            "trailing_stop_pct": 0.02
        },
        "medium": {
            "position_size_pct": 0.07,
            "stop_loss_pct": 0.07,
            "take_profit_pct": 0.15,
            "max_drawdown_pct": 0.20,
            "trailing_stop_pct": 0.03
        },
        "low": {
            "position_size_pct": 0.02,
            "stop_loss_pct": 0.02,
            "take_profit_pct": 0.05,
            "max_drawdown_pct": 0.10,
            "trailing_stop_pct": 0.02
        }
    }
    profile = profile.lower()
    if profile not in risk_profiles:
        raise ValueError("Risk profile must be 'high', 'medium', or 'low'.")
    return risk_profiles[profile]

def compute_sharpe_ratio(balance_history, risk_free_rate=0.0):
    """
    Compute the Sharpe ratio given a series of portfolio balances.

    Parameters:
        balance_history (list or np.array): Portfolio balance over time.
        risk_free_rate (float): Risk-free rate (default=0.0).

    Returns:
        float: Sharpe ratio.
    """
    returns = []
    for i in range(1, len(balance_history)):
        ret = (balance_history[i] - balance_history[i-1]) / balance_history[i-1]
        returns.append(ret)
    returns = np.array(returns)
    mean_return = np.mean(returns) - risk_free_rate
    std_return = np.std(returns) + 1e-9
    return mean_return / std_return

def compute_max_drawdown(balance_history):
    """
    Compute the maximum drawdown from the balance history.

    Parameters:
        balance_history (list or np.array): Portfolio balance over time.

    Returns:
        float: Maximum drawdown (as a fraction of the peak balance).
    """
    peak = balance_history[0]
    max_dd = 0.0
    for x in balance_history:
        if x > peak:
            peak = x
        dd = (peak - x) / peak
        max_dd = max(max_dd, dd)
    return max_dd

def simulate_ensemble_profit_with_risk(df_data, rl_model, rl_weight, strategy_weight, transformer_weight,
                                       initial_balance, scaling, risk_params, lookback):
    """
    Simulate ensemble trading over historical data while applying risk management.

    Parameters:
      df_data (DataFrame): DataFrame containing columns 'close', 'return', 'SMA_14', and 'RSI_14'.
      rl_model: Trained RL model.
      rl_weight (float): Weight for the RL model's decision.
      strategy_weight (float): Weight for the aggregated strategy signals.
      transformer_weight (float): Weight for the transformer model's decision.
      initial_balance (float): Starting portfolio balance.
      scaling (float): Scaling factor to convert returns into monetary terms.
      risk_params (dict): Risk management parameters.
      lookback (int): Lookback window for the transformer decision.

    Returns:
      tuple: (final_balance, balance_history)

    Note:
      This function calls the ensemble decision function (from strategies.ensemble)
      using the full DataFrame and the current index.
    """
    # Import ensemble decision function from the strategies module.
    from strategies.ensemble import ensemble_final_decision

    if risk_params is None:
        risk_params = get_risk_profile("high")
        
    balance = initial_balance
    peak_balance = balance
    balance_history = [balance]
    
    # Iterate over each row of the DataFrame.
    for i in range(len(df_data)):
        # Extract state vector from the DataFrame.
        state = df_data[['close', 'SMA_10', 'RSI_14']].iloc[i].values
        ret = df_data['return'].iloc[i]
        # Call ensemble_final_decision with the full DataFrame and current index.
        action = ensemble_final_decision(state, df_data, i, rl_model, rl_weight, strategy_weight, transformer_weight, lookback)
        if action not in [-1, 0, 1]:
            raise ValueError(f"Ensemble final decision returned invalid action {action}")
        
        raw_pnl = action * ret * scaling
        trade_size = balance * risk_params["position_size_pct"]
        max_loss = -trade_size * risk_params["stop_loss_pct"]
        max_gain = trade_size * risk_params["take_profit_pct"]
        actual_pnl = np.clip(raw_pnl, max_loss, max_gain)
        balance += actual_pnl
        
        if balance > peak_balance:
            peak_balance = balance
        drawdown = 1.0 - (balance / peak_balance)
        if drawdown > risk_params["max_drawdown_pct"]:
            risk_params["position_size_pct"] = max(risk_params["position_size_pct"] - 0.005, 0.01)
        
        balance_history.append(balance)
        print(f"[DEBUG] Step={i}, action={action}, return={ret:.4f}, raw_pnl={raw_pnl:.2f}, actual_pnl={actual_pnl:.2f}, balance={balance:.2f}")
    
    return balance, balance_history
