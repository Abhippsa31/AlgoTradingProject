import csv
import os

def save_trade_log(trades, output_path='output/trade_logs.csv'):
    os.makedirs("output", exist_ok=True)
    with open(output_path, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Buy_Date', 'Ticker', 'Buy_Price', 'Sell_Price', 'PnL'])
        writer.writeheader()
        for trade in trades:
            writer.writerow(trade)
