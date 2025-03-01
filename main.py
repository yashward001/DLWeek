# main.py
from data.realtime_data_pipeline import run_realtime_data_pipeline
from sentiment.sentiment_analysis import run_perplexity_sentiment_pipeline
from models.rl_model import load_or_train_rl_model, get_rl_prediction
from models.transformer_model import transformer_model, get_transformer_decision
from strategies.ensemble import ensemble_final_decision
from risk.risk_management import get_risk_profile, simulate_ensemble_profit_with_risk
from utils.visualisation import plot_balance_history

def main():
    print("=== Real-Time Data Pipeline ===")
    # Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual API key.
    api_key = "W5LXPX0X4CVPIHLX"
    symbol = "AAPL"
    final_df = run_realtime_data_pipeline(api_key, symbol)
    print("Fetched and processed real-time data (1hr interval):")
    print(final_df.tail())
    
    print("\n=== Sentiment Analysis Pipeline ===")
    # Replace None with your actual Perplexity API key if available.
    sentiment_data = run_perplexity_sentiment_pipeline(symbol, api_key=None)
    if sentiment_data.empty:
        sentiment_score = 0.5
        print("No sentiment data available, defaulting to neutral sentiment score: 0.5")
    else:
        sentiment_score = sentiment_data["perplexity_sentiment_avg"].iloc[0]
        print("Sentiment Score from Analysis:", sentiment_score)
    
    print("\n=== RL Model Loading/Training ===")
    # Use features from final_df: here we use "close", "SMA_10", and "RSI_14".
    # (Ensure your realtime data pipeline computes these indicators.)
    X_rl = final_df[["close", "SMA_10", "RSI_14"]].values
    returns_rl = final_df["return"].values
    model_path = "models/trained_rl_model_final.zip"
    rl_model = load_or_train_rl_model(X_rl, returns_rl, initial_balance=10000, total_timesteps=50000, model_path=model_path)
    
    print("\n=== Risk-Managed Ensemble Trading Simulation ===")
    risk_input = input("Enter risk profile (high, medium, low): ").strip()
    risk_params = get_risk_profile(risk_input)
    print("\nSelected Risk Management Parameters:")
    for key, value in risk_params.items():
        print(f"  {key}: {value}")
    
    # Run the ensemble simulation. The ensemble decision function uses the full DataFrame and current index.
    final_balance, ensemble_history = simulate_ensemble_profit_with_risk(
        df_data=final_df,
        rl_model=rl_model,
        rl_weight=0.33,
        strategy_weight=0.33,
        transformer_weight=0.34,
        initial_balance=10000,
        scaling=1000,
        risk_params=risk_params,
        lookback=20
    )
    profit = final_balance - 10000
    print(f"\nRisk-Managed Ensemble Final Balance: {final_balance:.2f}, Profit: {profit:.2f}")
    
    print("\n=== Visualisation ===")
    plot_balance_history(ensemble_history, title="Ensemble Trading Account Balance")

if __name__ == "__main__":
    main()
