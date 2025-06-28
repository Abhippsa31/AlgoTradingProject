from core.indicators import calculate_rsi, calculate_macd, calculate_moving_averages

def generate_signals(df):
 
    df['RSI'] = calculate_rsi(df['Close'])
    df['MACD'] = calculate_macd(df['Close'])
    
    df = calculate_moving_averages(df)
    
    df['Buy'] = (df['RSI'] < 55) & (df['MA_20'] > df['MA_50']) & (df['MACD'] > 0)

    print(f" Buy Signals Generated: {df['Buy'].sum()}")
    return df