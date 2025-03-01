# strategies/ensemble.py
import numpy as np
import pandas as pd
# Import helper functions from the models folder (make sure your PYTHONPATH is set correctly)
from models.rl_model import get_rl_prediction
from models.transformer_model import get_transformer_decision

# ------------------------------
# Trading Strategy Functions
# ------------------------------
def momentum_crossover_strategy(state):
    ret = state[1]
    return -1 if ret < -0.01 else (1 if ret > 0.01 else 0)

def moving_average_crossover_strategy(state):
    price = state[0]
    return -1 if price > 150 else (1 if price < 120 else 0)

def bollinger_bands_breakout_strategy(state):
    price = state[0]
    return -1 if price > 160 else (1 if price < 110 else 0)

def mean_reversion_strategy(state):
    price = state[0]
    z_score = (price - 130) / 10
    return -1 if z_score > 1 else (1 if z_score < -1 else 0)

def vwap_strategy(state):
    price = state[0]
    return -1 if price > 140 else (1 if price < 120 else 0)

def adx_trend_confirmation_strategy(state):
    ret = state[1]
    return 1 if ret > 0.02 else (-1 if ret < -0.02 else 0)

def ichimoku_cloud_strategy(state):
    return np.random.choice([-1, 0, 1])

def stochastic_oscillator_strategy(state):
    ret = state[1]
    return 1 if ret > 0.015 else (-1 if ret < -0.015 else 0)

def candlestick_pattern_strategy(state):
    return np.random.choice([-1, 0, 1])

def ensemble_ml_strategy(state):
    ret = state[1]
    return 1 if ret > 0.01 else (-1 if ret < -0.01 else 0)

def pivot_points_strategy(state):
    price = state[0]
    pivot = 130
    return -1 if price > pivot + 10 else (1 if price < pivot - 10 else 0)

def volume_spike_divergence_strategy(state):
    ret = state[1]
    return 1 if ret > 0.02 else (-1 if ret < -0.02 else 0)

def multi_timeframe_confirmation_strategy(state):
    decision1 = 1 if state[0] > 130 else -1
    decision2 = 1 if state[1] > 0.005 else -1
    return decision1 if decision1 == decision2 else 0

def advanced_momentum_volatility_strategy(state):
    ret = state[1]
    return 1 if ret > 0.02 else (-1 if ret < -0.02 else 0)

# ------------------------------
# List of Strategy Functions and Their Names
# ------------------------------
strategy_functions = [
    momentum_crossover_strategy,
    moving_average_crossover_strategy,
    bollinger_bands_breakout_strategy,
    mean_reversion_strategy,
    vwap_strategy,
    adx_trend_confirmation_strategy,
    ichimoku_cloud_strategy,
    stochastic_oscillator_strategy,
    candlestick_pattern_strategy,
    ensemble_ml_strategy,
    pivot_points_strategy,
    volume_spike_divergence_strategy,
    multi_timeframe_confirmation_strategy,
    advanced_momentum_volatility_strategy,
]

strategy_names = [
    "Momentum Crossover",
    "Moving Average Crossover",
    "Bollinger Bands Breakout",
    "Mean Reversion",
    "VWAP",
    "ADX Trend Confirmation",
    "Ichimoku Cloud",
    "Stochastic Oscillator",
    "Candlestick Pattern",
    "Ensemble ML",
    "Pivot Points",
    "Volume Spike & Divergence",
    "Multi Timeframe Confirmation",
    "Advanced Momentum & Volatility",
]

# ------------------------------
# Ensemble Helper Functions
# ------------------------------
def compute_all_strategy_signals(state):
    """
    Compute the signal from each strategy given a state vector.
    
    Returns:
        dict: Mapping from strategy name to (signal, confidence).
              (Confidence is set to 1.0 by default.)
    """
    signals = {}
    for name, func in zip(strategy_names, strategy_functions):
        signals[name] = (func(state), 1.0)
    return signals

def aggregate_strategy_signals(state):
    """
    Aggregate the individual strategy signals by summing and taking the sign.
    
    Returns:
        int: 1 if positive (Buy), -1 if negative (Sell), or 0 (Hold).
    """
    signals_dict = compute_all_strategy_signals(state)
    total = sum(signal for signal, conf in signals_dict.values())
    return 1 if total > 0 else (-1 if total < 0 else 0)

def ensemble_final_decision(state, df, current_index, rl_model, rl_weight=0.33, strategy_weight=0.33, transformer_weight=0.34, lookback=20):
    """
    Compute the final ensemble trading decision by combining decisions from:
      - The RL model,
      - The aggregated strategy signals,
      - The transformer meta-model.
    
    Parameters:
        state (np.array): The current state vector.
        df (DataFrame): Full DataFrame containing necessary columns.
        current_index (int): Current index in the DataFrame (for transformer input).
        rl_model: Trained RL model.
        rl_weight (float): Weight for the RL model's decision.
        strategy_weight (float): Weight for the aggregated strategy signals.
        transformer_weight (float): Weight for the transformer decision.
        lookback (int): Lookback window for transformer decision.
    
    Returns:
        int: Final decision (-1, 0, or 1).
    """
    rl_action = get_rl_prediction(rl_model, state)
    strategy_action = aggregate_strategy_signals(state)
    transformer_action = get_transformer_decision(df, current_index, lookback)
    combined_value = (rl_weight * rl_action +
                      strategy_weight * strategy_action +
                      transformer_weight * transformer_action)
    return 1 if combined_value > 0.2 else (-1 if combined_value < -0.2 else 0)

# ------------------------------
# Example Usage (for testing)
# ------------------------------
if __name__ == "__main__":
    # Create a sample state vector with three features: [close, return, RSI_14]
    sample_state = np.array([135.0, 0.012, 55.0])
    
    # For demonstration, create a dummy DataFrame with required columns.
    # Here, we use "SMA_10" as a placeholder for the moving average.
    df_dummy = pd.DataFrame({
        "close": [135.0] * 30,
        "SMA_10": [130.0] * 30,
        "RSI_14": [55.0] * 30,
        "return": [0.012] * 30
    })
    
    # Compute individual strategy signals and aggregate them.
    all_signals = compute_all_strategy_signals(sample_state)
    agg_signal = aggregate_strategy_signals(sample_state)
    
    # For demonstration, assume we have a trained RL model.
    # In practice, replace dummy_rl_model with your actual trained model.
    dummy_rl_model = None  
    # And use the dummy DataFrame's last index (e.g., 29) for the transformer decision.
    final_decision = ensemble_final_decision(sample_state, df_dummy, current_index=29, rl_model=dummy_rl_model)
    
    print("Individual Strategy Signals:")
    for name, (signal, conf) in all_signals.items():
        print(f"{name}: {'Buy' if signal == 1 else 'Sell' if signal == -1 else 'Hold'}")
    print("Aggregated Strategy Decision:", "Buy" if agg_signal == 1 else "Sell" if agg_signal == -1 else "Hold")
    print("Ensemble Final Decision:", "Buy" if final_decision == 1 else "Sell" if final_decision == -1 else "Hold")
