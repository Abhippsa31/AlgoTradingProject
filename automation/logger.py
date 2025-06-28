import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from config.settings import SHEET_NAME, TRADE_TAB, SUMMARY_TAB, GOOGLE_CREDS_PATH

def connect_sheet(sheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDS_PATH, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def log_trade_data(sheet_name, stock, trades):
    sheet = connect_sheet(sheet_name)
    worksheet = sheet.worksheet(TRADE_TAB)

    for trade in trades:
        row = [stock, trade['Buy_Date'], trade['Buy_Price'], trade['Sell_Price'], trade['PnL']]
        worksheet.append_row(row, value_input_option="USER_ENTERED")

def log_summary_pnl(sheet_name, summary_data):
    sheet = connect_sheet(sheet_name)
    worksheet = sheet.worksheet(SUMMARY_TAB)
    worksheet.clear()
    worksheet.append_row(["Stock", "Total Trades", "Winning Trades", "Losing Trades", "Total PnL"])

    for stock, summary in summary_data.items():
        row = [
            stock,
            summary["total"],
            summary["wins"],
            summary["losses"],
            round(summary["pnl"], 2)
        ]
        worksheet.append_row(row, value_input_option="USER_ENTERED")

def log_win_ratio(sheet_name, summary_data):
    sheet = connect_sheet(sheet_name)
    if "win_ratio" not in [ws.title for ws in sheet.worksheets()]:
        sheet.add_worksheet(title="win_ratio", rows="10", cols="2")
    worksheet = sheet.worksheet("win_ratio")
    worksheet.clear()
    worksheet.append_row(["Stock", "Win Ratio"])

    for stock, summary in summary_data.items():
        win_ratio = (summary["wins"] / summary["total"]) if summary["total"] > 0 else 0.0
        worksheet.append_row([stock, round(win_ratio * 100, 2)], value_input_option="USER_ENTERED")

def log_model_accuracy(sheet_name, model_accuracies):
    sheet = connect_sheet(sheet_name)
    if "Model_Accuracy" not in [ws.title for ws in sheet.worksheets()]:
        sheet.add_worksheet(title="Model_Accuracy", rows="10", cols="2")
    worksheet = sheet.worksheet("Model_Accuracy")
    worksheet.clear()
    worksheet.append_row(["Stock", "Accuracy (%)"])

    for stock, accuracy in model_accuracies.items():
        worksheet.append_row([stock, accuracy], value_input_option="USER_ENTERED")

