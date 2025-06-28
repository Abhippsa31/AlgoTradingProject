from sklearn.model_selection import train_test_split, TimeSeriesSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from core.indicators import calculate_rsi, calculate_macd
import pandas as pd
import numpy as np
import joblib
import os

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

def prepare_ml_data(df, stock=None):
    try:
        
        required_cols = ['Close', 'Volume']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        
        df['RSI'] = calculate_rsi(df['Close'])
        df['MACD'] = calculate_macd(df['Close'])

        
        df.dropna(subset=['RSI', 'MACD', 'Close', 'Volume'], inplace=True)

        
        df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
        df.dropna(subset=['Target'], inplace=True)

        if df.empty or len(df) < 10:
            print(f"⚠️ Not enough clean data for {stock}")
            return None, None

        X = df[['RSI', 'MACD', 'Volume']]
        y = df['Target']
        return X, y

    except Exception as e:
        print(f"Data Prep Error for {stock}: {e}")
        return None, None


def train_predict_model(df, ticker, retrain=False):
    
    try:
        model_path = os.path.join(MODEL_DIR, f"{ticker}_model.pkl")

        
        if not retrain and os.path.exists(model_path):
            model = joblib.load(model_path)
            X, y = prepare_ml_data(df, ticker)
            if X is None or y is None:
                return None, None
            predictions = model.predict(X)
            accuracy = accuracy_score(y, predictions)
            return model, round(accuracy * 100, 2)

        
        X, y = prepare_ml_data(df, ticker)
        if X is None or y is None:
            return None, None

        
        tscv = TimeSeriesSplit(n_splits=3)
        accuracies = []

        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', DecisionTreeClassifier(
                max_depth=5,
                min_samples_split=10,
                random_state=42
            ))
        ])

        for train_idx, test_idx in tscv.split(X):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

            pipeline.fit(X_train, y_train)
            preds = pipeline.predict(X_test)
            accuracies.append(accuracy_score(y_test, preds))

        
        pipeline.fit(X, y)
        joblib.dump(pipeline, model_path)

        mean_accuracy = np.mean(accuracies) * 100
        return pipeline, round(mean_accuracy, 2)

    except Exception as e:
        print(f"Model training error for {ticker}: {str(e)}")
        return None, None
