# transformer_model.py
import torch
import torch.nn as nn
import math
import numpy as np
import pandas as pd

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        """
        Implements sinusoidal positional encoding.
        
        Args:
            d_model (int): Embedding dimension.
            dropout (float): Dropout rate.
            max_len (int): Maximum length of sequence.
        """
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        pe = torch.zeros(max_len, d_model)  # (max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)  # (max_len, 1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)  # even indices
        pe[:, 1::2] = torch.cos(position * div_term)  # odd indices
        pe = pe.unsqueeze(0)  # (1, max_len, d_model)
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        # x shape: (batch, seq_len, d_model)
        x = x + self.pe[:, :x.size(1)]
        return self.dropout(x)

class TransformerMetaModelWithProfit(nn.Module):
    def __init__(self, input_dim=29, embed_dim=64, nhead=8, num_layers=3, dropout=0.1, num_classes=3):
        """
        Transformer meta‑model that fuses multiple signals to produce a trading decision 
        and an estimated profitability.
        
        Args:
            input_dim (int): Number of features per time step (e.g., 29: 14 signals, 14 profitability metrics, 1 sentiment).
            embed_dim (int): Dimension of the transformer embeddings.
            nhead (int): Number of attention heads.
            num_layers (int): Number of transformer encoder layers.
            dropout (float): Dropout rate.
            num_classes (int): Number of classes for classification (e.g., 3 for Sell, Hold, Buy).
        """
        super(TransformerMetaModelWithProfit, self).__init__()
        self.embedding = nn.Linear(input_dim, embed_dim)
        self.pos_encoder = PositionalEncoding(embed_dim, dropout)
        encoder_layer = nn.TransformerEncoderLayer(d_model=embed_dim, nhead=nhead, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc_decision = nn.Linear(embed_dim, num_classes)  # Classification head (decision)
        self.fc_profit = nn.Linear(embed_dim, 1)              # Regression head (profitability)
    
    def forward(self, x):
        """
        Forward pass.
        
        Args:
            x (Tensor): Input tensor of shape (batch, seq_len, input_dim)
            
        Returns:
            decision_logits (Tensor): Logits for trading decision (batch, num_classes)
            profit_output (Tensor): Profitability output (batch, 1)
        """
        x = self.embedding(x)           # (batch, seq_len, embed_dim)
        x = self.pos_encoder(x)         # (batch, seq_len, embed_dim)
        x = x.transpose(0, 1)           # (seq_len, batch, embed_dim) for transformer
        transformer_out = self.transformer_encoder(x)  # (seq_len, batch, embed_dim)
        pooled = transformer_out.mean(dim=0)           # (batch, embed_dim) via mean pooling
        decision_logits = self.fc_decision(pooled)       # (batch, num_classes)
        profit_output = self.fc_profit(pooled)           # (batch, 1)
        return decision_logits, profit_output

# Instantiate the transformer meta-model.
transformer_model = TransformerMetaModelWithProfit()

def get_transformer_input(df, index, lookback=20, sentiment_score=0.0):
    """
    Build a 29-dimensional input for the transformer model using a lookback window from df.
    
    For each time step in the window ending at 'index', the feature vector is composed of:
      - 14 strategy signals (dummy here: simulated as sign(RSI_14 - 50) repeated 14 times),
      - 14 profitability metrics (dummy: repeated 'return' value),
      - 1 sentiment score (provided externally).
      
    Args:
        df (DataFrame): DataFrame containing at least the columns 'close', 'SMA_14', 'RSI_14', 'return'.
        index (int): End index of the lookback window.
        lookback (int): Number of time steps.
        sentiment_score (float): Sentiment score to include.
        
    Returns:
        Tensor: Input tensor of shape (1, lookback, 29).
    """
    input_list = []
    # For each row in the lookback window:
    for i in range(index - lookback + 1, index + 1):
        state = df[['close', 'SMA_10', 'RSI_14']].iloc[i].values
        # Dummy strategy signals: for demo, use sign(RSI_14 - 50) repeated 14 times.
        rsi = state[2]
        signal = 1 if rsi > 50 else -1
        signals = [signal] * 14
        # Profitability metrics: dummy by repeating the 'return' value 14 times.
        profitability = [df['return'].iloc[i]] * 14
        # Sentiment: use the provided sentiment score.
        sentiment = [sentiment_score]
        feature_vector = signals + profitability + sentiment  # Total length = 14 + 14 + 1 = 29.
        input_list.append(feature_vector)
    input_array = np.array(input_list, dtype=np.float32)
    # Convert to tensor and add batch dimension: (1, lookback, 29)
    return torch.tensor(input_array).unsqueeze(0)

def get_transformer_decision(df, index, lookback=20, sentiment_score=0.0):
    """
    Run the transformer model on a lookback window ending at 'index' and return a trading decision.
    
    Returns:
        int: Decision mapping: -1 (Sell), 0 (Hold), or 1 (Buy).
    """
    transformer_input = get_transformer_input(df, index, lookback, sentiment_score)
    decision_logits, _ = transformer_model(transformer_input)
    decision_class = torch.argmax(decision_logits, dim=1).item()
    mapping = {0: -1, 1: 0, 2: 1}
    return mapping.get(decision_class, 0)

if __name__ == "__main__":
    # Example usage:
    # Create a dummy DataFrame with necessary columns
    dates = pd.date_range(start="2022-01-01", periods=50, freq="H")
    data = {
        "close": np.random.uniform(100, 200, size=50),
        "SMA_10": np.random.uniform(100, 200, size=50),
        "RSI_14": np.random.uniform(0, 100, size=50),
        "return": np.random.uniform(-0.01, 0.01, size=50)
    }
    df_dummy = pd.DataFrame(data, index=dates)
    
    # Get transformer input and decision for the last row with a lookback of 20 and sentiment score 0.5
    transformer_in = get_transformer_input(df_dummy, index=len(df_dummy)-1, lookback=20, sentiment_score=0.5)
    decision = get_transformer_decision(df_dummy, index=len(df_dummy)-1, lookback=20, sentiment_score=0.5)
    print("Transformer input shape:", transformer_in.shape)
    print("Transformer decision:", decision)
