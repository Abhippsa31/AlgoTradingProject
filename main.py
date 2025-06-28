import pandas as pd  
from core.data_fetcher import fetch_stock_data
from core.strategy import generate_signals
from core.backtester import backtest_strategy
from automation.logger import log_model_accuracy
from core.ml_model import train_predict_model
from automation.logger import (
    log_trade_data,
    log_summary_pnl,
    log_win_ratio,
)

def main():
    stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']
    sheet_name = "AlgoTradeLog"
    summary_data = {}
    model_accuracies = {}
    
    INITIAL_BALANCE = 100000

    print("\n Starting Algo Trading Strategy...\n")

    for stock in stocks:
        print(f"\n Processing: {stock}")
        data = fetch_stock_data(stock)

        if data is None or data.empty or len(data) < 30:
            print(f" Insufficient data for {stock} ({len(data) if data else 0} records)")
            continue
        
        data = generate_signals(data)
        trades, final_balance = backtest_strategy(data)

        print(f"Trades: {len(trades)} | Final Balance: ₹{final_balance:.2f}")

        if trades:
            wins = sum(1 for t in trades if t["PnL"] > 0)
            losses = sum(1 for t in trades if t["PnL"] <= 0)
            total_pnl = sum(t["PnL"] for t in trades)
            
            avg_win = sum(t["PnL"] for t in trades if t["PnL"] > 0)/max(1,wins)
            avg_loss = sum(t["PnL"] for t in trades if t["PnL"] <= 0)/max(1,losses)
            print(f"   Win Rate: {wins/len(trades):.1%} | Avg Win: ₹{avg_win:.2f} | Avg Loss: ₹{avg_loss:.2f}")
            
            log_trade_data(sheet_name, stock, trades)
        else:
            print(f" No trades executed for {stock}")
            wins, losses, total_pnl = 0, 0, 0

        summary_data[stock] = {
            "total": len(trades),
            "wins": wins,
            "losses": losses,
            "pnl": total_pnl
        }

        try:
            model, accuracy = train_predict_model(data, stock)
            if accuracy is not None:
                model_accuracies[stock] = accuracy
                print(f" ML Accuracy for {stock}: {accuracy}%")
            else:
                print(f" ML Model skipped for {stock} (data preparation issue)")
        except Exception as e:
            print(f" ML Model failed for {stock}: {str(e)}")

    log_summary_pnl(sheet_name, summary_data)
    log_win_ratio(sheet_name, summary_data)
    log_model_accuracy(sheet_name, model_accuracies)  

    print("\n Strategy Performance:")
    final_total = sum(s["pnl"] for s in summary_data.values()) + INITIAL_BALANCE
    print(f" Total Trades: {sum(s['total'] for s in summary_data.values())}")
    print(f" Overall PnL: ₹{final_total - INITIAL_BALANCE:,.2f} ({((final_total/INITIAL_BALANCE)-1):.1%})")

    print("\n Strategy run complete. Check Google Sheets for logs.\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f" ERROR: {e}")