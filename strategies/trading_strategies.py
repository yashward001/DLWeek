# trading_strategies.py
import numpy as np

def momentum_crossover_strategy(state):
    """
    Returns -1 if return < -0.01 (Sell), 1 if return > 0.01 (Buy), else 0 (Hold).
    """
    ret = state[1]
    if ret < -0.01:
        return -1
    elif ret > 0.01:
        return 1
    else:
        return 0

def moving_average_crossover_strategy(state):
    """
    Returns -1 if price > 150 (Sell), 1 if price < 120 (Buy), else 0 (Hold).
    """
    price = state[0]
    if price > 150:
        return -1
    elif price < 120:
        return 1
    else:
        return 0

def bollinger_bands_breakout_strategy(state):
    """
    Returns -1 if price > 160 (Sell), 1 if price < 110 (Buy), else 0 (Hold).
    """
    price = state[0]
    if price > 160:
        return -1
    elif price < 110:
        return 1
    else:
        return 0

def mean_reversion_strategy(state):
    """
    Uses z-score of price (with assumed mean 130 and std 10).
    Returns -1 if z_score > 1 (Sell), 1 if z_score < -1 (Buy), else 0 (Hold).
    """
    price = state[0]
    z_score = (price - 130) / 10
    if z_score > 1:
        return -1
    elif z_score < -1:
        return 1
    else:
        return 0

def vwap_strategy(state):
    """
    Returns -1 if price > 140 (Sell), 1 if price < 120 (Buy), else 0 (Hold).
    """
    price = state[0]
    if price > 140:
        return -1
    elif price < 120:
        return 1
    else:
        return 0

def adx_trend_confirmation_strategy(state):
    """
    Returns 1 if return > 0.02 (Buy), -1 if return < -0.02 (Sell), else 0 (Hold).
    """
    ret = state[1]
    if ret > 0.02:
        return 1
    elif ret < -0.02:
        return -1
    else:
        return 0

def ichimoku_cloud_strategy(state):
    """
    Placeholder: Returns a random decision.
    """
    return np.random.choice([-1, 0, 1])

def stochastic_oscillator_strategy(state):
    """
    Returns 1 if return > 0.015 (Buy), -1 if return < -0.015 (Sell), else 0 (Hold).
    """
    ret = state[1]
    if ret > 0.015:
        return 1
    elif ret < -0.015:
        return -1
    else:
        return 0

def candlestick_pattern_strategy(state):
    """
    Placeholder: Returns a random decision.
    """
    return np.random.choice([-1, 0, 1])

def ensemble_ml_strategy(state):
    """
    Returns 1 if return > 0.01 (Buy), -1 if return < -0.01 (Sell), else 0 (Hold).
    """
    ret = state[1]
    if ret > 0.01:
        return 1
    elif ret < -0.01:
        return -1
    else:
        return 0

def pivot_points_strategy(state):
    """
    Returns -1 if price > (pivot+10), 1 if price < (pivot-10), else 0.
    Here pivot is assumed to be 130.
    """
    price = state[0]
    pivot = 130
    if price > pivot + 10:
        return -1
    elif price < pivot - 10:
        return 1
    else:
        return 0

def volume_spike_divergence_strategy(state):
    """
    Returns 1 if return > 0.02 (Buy), -1 if return < -0.02 (Sell), else 0 (Hold).
    """
    ret = state[1]
    if ret > 0.02:
        return 1
    elif ret < -0.02:
        return -1
    else:
        return 0

def multi_timeframe_confirmation_strategy(state):
    """
    Uses two simple conditions:
      - Condition 1: 1 if price > 130, else -1.
      - Condition 2: 1 if return > 0.005, else -1.
    Returns the decision if both conditions agree; otherwise returns 0.
    """
    decision1 = 1 if state[0] > 130 else -1
    decision2 = 1 if state[1] > 0.005 else -1
    return decision1 if decision1 == decision2 else 0

def advanced_momentum_volatility_strategy(state):
    """
    Returns 1 if return > 0.02 (Buy), -1 if return < -0.02 (Sell), else 0 (Hold).
    """
    ret = state[1]
    if ret > 0.02:
        return 1
    elif ret < -0.02:
        return -1
    else:
        return 0

if __name__ == "__main__":
    # Example usage: assume a state vector with [close, return, RSI_14]
    sample_state = np.array([135.0, 0.012, 55.0])
    print("Trading Strategy Signals for the sample state:")
    print("Momentum Crossover:", momentum_crossover_strategy(sample_state))
    print("Moving Average Crossover:", moving_average_crossover_strategy(sample_state))
    print("Bollinger Bands Breakout:", bollinger_bands_breakout_strategy(sample_state))
    print("Mean Reversion:", mean_reversion_strategy(sample_state))
    print("VWAP:", vwap_strategy(sample_state))
    print("ADX Trend Confirmation:", adx_trend_confirmation_strategy(sample_state))
    print("Ichimoku Cloud:", ichimoku_cloud_strategy(sample_state))
    print("Stochastic Oscillator:", stochastic_oscillator_strategy(sample_state))
    print("Candlestick Pattern:", candlestick_pattern_strategy(sample_state))
    print("Ensemble ML:", ensemble_ml_strategy(sample_state))
    print("Pivot Points:", pivot_points_strategy(sample_state))
    print("Volume Spike & Divergence:", volume_spike_divergence_strategy(sample_state))
    print("Multi Timeframe Confirmation:", multi_timeframe_confirmation_strategy(sample_state))
    print("Advanced Momentum & Volatility:", advanced_momentum_volatility_strategy(sample_state))
