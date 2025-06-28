import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="6mo", interval="1d"):
    try:
        print(f" Fetching data for {ticker} (Period: {period}, Interval: {interval})")
        df = yf.download(ticker, period=period, interval=interval)

        if df.empty:
            print(f" No data found for {ticker}")
            return None

        
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0] for col in df.columns]

        
        df.rename(columns=lambda x: x.strip().title(), inplace=True)

        
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f" Missing required columns: {missing_cols}")
            return None

        df.reset_index(inplace=True)

        print(f" Columns for {ticker}: {df.columns.tolist()}")
        return df

    except Exception as e:
        print(f" Error fetching data for {ticker}: {e}")
        return None
