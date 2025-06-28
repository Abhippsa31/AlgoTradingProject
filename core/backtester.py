def backtest_strategy(data, initial_balance=100000):
    balance = float(initial_balance)
    position = False
    trades = []

    for i in range(len(data) - 1):
        try:
            
            if bool(data['Buy'].iloc[i]) and not position:
                buy_price = float(data['Close'].iloc[i])
                sell_price = float(data['Close'].iloc[i + 1])
                pnl = round(sell_price - buy_price, 2)
                balance = round(balance + pnl, 2)
                position = True

                buy_date = data.iloc[i].get("Date") if "Date" in data.columns else data.index[i]
                buy_date_str = str(buy_date.date()) if hasattr(buy_date, "date") else str(buy_date)

                trades.append({
                    'Buy_Date': buy_date_str,
                    'Buy_Price': round(buy_price, 2),
                    'Sell_Price': round(sell_price, 2),
                    'PnL': pnl
                })

                position = False

        except Exception as e:
            print(f" Skipping row {i}: {e}")
            continue

    return trades, balance
