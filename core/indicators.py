import pandas as pd
import numpy as np

def calculate_moving_averages(df, windows=[20, 50]):
    
    try:
        df = df.copy()
        for window in windows:
            col_name = f'MA_{window}'
            df[col_name] = df['Close'].rolling(window=window, min_periods=1).mean()
        return df
    except Exception as e:
        print(f"Moving Averages Error: {str(e)}")
        return df

def calculate_rsi(series, period=14):
    
    try:
        if isinstance(series, (pd.DataFrame, np.ndarray)):
            series = pd.Series(series.squeeze())
        delta = series.diff()
        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
        avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    except Exception as e:
        print(f"RSI Error: {str(e)}")
        return pd.Series(50, index=series.index)  

def calculate_macd(series, fast=12, slow=26):
    
    try:
        if isinstance(series, (pd.DataFrame, np.ndarray)):
            series = pd.Series(series.squeeze())
        ema_fast = series.ewm(span=fast, adjust=False).mean()
        ema_slow = series.ewm(span=slow, adjust=False).mean()
        macd = ema_fast - ema_slow
        return macd
    except Exception as e:
        print(f"MACD Error: {str(e)}")
        return pd.Series(0, index=series.index)  
