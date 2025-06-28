AlgoTradingProject
Algo-Trading System with ML; Google Sheets Integration.
This project is a Python-based mini algorithmic trading prototype that demonstrates a rule-based trading strategy enhanced with basic machine learning and automation. The system fetches live stock data using yfinance, generates trading signals using technical indicators like RSI and Moving Averages, backtests the strategy, and logs results into Google Sheets.

Additionally, it uses a Decision Tree classifier to predict the next-day market movement based on indicators like RSI, MACD, and Volume, and reports the prediction accuracy per stock.
Key Features
Stock Data Ingestion – Downloads historical stock prices from Yahoo Finance for selected NIFTY 50 stocks.
Strategy Logic – Implements a simple RSI + DMA crossover strategy:

Buy signal: RSI < 30 and 20-DMA > 50-DMA

Backtesting – Simulates strategy performance over 6 months to compute PnL and win/loss count.
ML Automation (Bonus) – Uses a Decision Tree to predict next-day price movement with accuracy reporting.
Google Sheets Logging – Automatically logs:
Trade history (Trade_Log tab)
Summary PnL (Summary_PnL tab)
Win ratio (win_ratio tab)
ML model accuracy (Model_Accuracy tab)

Console Output – Shows real-time progress, trade execution, and prediction accuracy.

Deliverables

Clean, modular Python code with reusable components (core/, automation/, config/)
Output stored both locally and in connected Google Sheets
ML experiment Jupyter Notebook included for model inspection
Short demo videos explaining the code flow and output behavior
