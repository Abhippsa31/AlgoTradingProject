# 📊 Algo-Trading System with ML & Google Sheets Integration

A Python-based algorithmic trading prototype that combines **technical indicators** and **machine learning** to generate signals, simulate trades, and log performance metrics to **Google Sheets**.

---

## 🚀 Features

✅ Rule-based strategy: RSI + 20/50 DMA crossover  
✅ ML-based prediction using Decision Tree  
✅ Backtesting and PnL calculation  
✅ Google Sheets automation for trade logs and model results  
✅ Jupyter Notebook included for experiments

---

## 🧠 Strategy Logic

### 💡 Buy Signal Criteria
```
RSI < 30 and 20-DMA > 50-DMA
```

### 📈 Technical Indicators
- **RSI (Relative Strength Index)**: Identifies oversold conditions
- **DMA (Daily Moving Averages)**: Confirms trend reversals

<img src="https://upload.wikimedia.org/wikipedia/commons/7/75/RSI_trading_chart.png" width="600" />

---

## 🧪 Machine Learning

- Features used: `RSI`, `MACD`, `Volume`
- Target: Next day price movement
- Model: `DecisionTreeClassifier`
- Evaluation: Time Series Cross-Validation

📊 Sample Output:

✅ ML Accuracy for TCS.NS: 52.34%
✅ ML Accuracy for INFY.NS: 48.78%


## 📋 Google Sheets Output

Each run logs results into 4 separate tabs:

| Tab Name        | Description                            |
|----------------|----------------------------------------|
| Trade_Log      | Detailed trades per stock              |
| Summary_PnL    | PnL summary per stock                  |
| win_ratio      | Percentage of winning trades           |
| Model_Accuracy | ML prediction accuracy for each stock  |

🔗 Example (Auto-filled via Sheets API):
![Google Sheet Example](https://i.imgur.com/9YAZ9lJ.png)

---

## 🧾 Folder Structure

algo_trading_project/
├── main.py                   # Entry point
├── core/                    # Strategy, backtest, indicators
├── automation/              # Google Sheets + Telegram (optional)
├── config/                  # Settings + credentials
├── output/                  # CSV/JSON/model outputs
├── notebooks/               # ML notebook
├── requirements.txt
└── README.md

## 📦 Install Dependencies

pip install -r requirements.txt
## ▶️ Run the Strategy

python main.py

## 🧠 Run ML Accuracy Checker

python ml_accuracy_checker.py

## 🎥 Demo Videos

**Video 1 – Code Overview & Logic**  
  [🔗 Google Drive Link](https://drive.google.com/your-link)

## 🙋‍♀️ Author
**Abhippsa Subhadarshini**  
💼 GitHub: [github.com/abhippsa](https://github.com/abhippsa)  
📧 Email: rimun390@example.com
