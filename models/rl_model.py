# rl_model.py
import os
import gym
from gym import spaces
import numpy as np
import random
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

class TradingEnv(gym.Env):
    """
    Custom trading environment for RL.
    
    Uses an array of features (e.g., [close, SMA_14, RSI_14]) and a corresponding
    array of returns. The action space is discrete:
      0: Sell → mapped to -1,
      1: Hold → mapped to 0,
      2: Buy  → mapped to 1.
    
    Reward is computed as:
        reward = action_sign * return * scaling_factor
    where a scaling factor (here 10,000) is applied.
    """
    metadata = {'render.modes': ['human']}
    
    def __init__(self, X, returns, initial_balance=10000):
        """
        Parameters:
            X (np.array): Feature array (shape: [num_steps, num_features]).
            returns (np.array): Array of returns for each time step.
            initial_balance (float): Starting balance.
        """
        super(TradingEnv, self).__init__()
        self.X = X
        self.returns = returns
        self.initial_balance = initial_balance
        self.action_space = spaces.Discrete(3)  # 0: Sell, 1: Hold, 2: Buy
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf,
                                            shape=(X.shape[1],), dtype=np.float32)
        self.reset()
    
    def reset(self):
        """
        Reset the environment: pick a random starting point in the first half of the data.
        """
        self.current_step = np.random.randint(0, len(self.X) // 2)
        self.balance = self.initial_balance
        return self.X[self.current_step]
    
    def step(self, action):
        """
        Take a step in the environment.
        
        Parameters:
            action (int): Action (0, 1, or 2).
            
        Returns:
            next_state (np.array), reward (float), done (bool), info (dict)
        """
        # Map action to trading direction: 0->Sell (-1), 1->Hold (0), 2->Buy (1)
        if action == 0:
            action_sign = -1
        elif action == 2:
            action_sign = 1
        else:
            action_sign = 0
        
        actual_return = self.returns[self.current_step]
        reward = action_sign * actual_return * 10000  # scaling factor
        self.balance += reward
        self.current_step += 1
        
        done = (self.current_step >= len(self.X) - 1)
        next_state = self.X[self.current_step] if not done else np.zeros(self.X.shape[1])
        return next_state, reward, done, {}
    
    def render(self, mode='human'):
        print(f"Step: {self.current_step}, Balance: {self.balance:.2f}")

def make_env(X, returns, initial_balance=10000):
    """
    Create a TradingEnv instance and wrap it with DummyVecEnv.
    """
    env = TradingEnv(X, returns, initial_balance=initial_balance)
    env = DummyVecEnv([lambda: env])
    return env

def train_rl_model(X, returns, initial_balance=10000, total_timesteps=50000, learning_rate=1e-3):
    """
    Train a DQN agent on the TradingEnv.
    """
    env = make_env(X, returns, initial_balance)
    model = DQN("MlpPolicy", env, verbose=1, learning_rate=learning_rate)
    model.learn(total_timesteps=total_timesteps)
    return model

def load_or_train_rl_model(X, returns, initial_balance=10000, total_timesteps=50000,
                           learning_rate=1e-3, model_path="models/trained_rl_model_final.zip"):
    """
    Load a pre-trained DQN model from disk if it exists; otherwise, train a new one and save it.
    """
    env = make_env(X, returns, initial_balance)
    if os.path.exists(model_path):
        print(f"Loading pre-trained model from {model_path}")
        model = DQN.load(model_path, env=env)
    else:
        print("No pre-trained model found. Training a new model...")
        model = train_rl_model(X, returns, initial_balance, total_timesteps, learning_rate)
        model.save(model_path)
    return model

def get_rl_prediction(model, state):
    """
    Given a trained RL model and a state, predict an action.
    Maps the DQN's discrete output {0,1,2} to {-1,0,1}.
    
    Parameters:
        model: Trained RL model.
        state (np.array): Single state vector.
    
    Returns:
        int: Mapped action (-1, 0, or 1).
    """
    state_input = state.reshape(1, -1) if len(state.shape) == 1 else state
    action, _ = model.predict(state_input, deterministic=True)
    if isinstance(action, np.ndarray):
        action = int(action[0])
    mapping = {0: -1, 1: 0, 2: 1}
    mapped_action = mapping.get(action, None)
    if mapped_action is None:
        raise ValueError(f"Unexpected RL action: {action}")
    return mapped_action

if __name__ == "__main__":
    # --- Example usage: simulate dummy data for demonstration.
    dummy_X = np.random.uniform(low=100, high=200, size=(100, 3))
    dummy_returns = np.random.uniform(low=-0.01, high=0.01, size=100)
    model_path = "models/trained_rl_model_final.zip"
    model = load_or_train_rl_model(dummy_X, dummy_returns, initial_balance=10000, total_timesteps=5000, model_path=model_path)
    sample_state = dummy_X[-1]
    action = get_rl_prediction(model, sample_state)
    print("Predicted RL action (mapped):", action)
