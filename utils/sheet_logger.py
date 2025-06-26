import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime


def log_to_sheet(ticker, date, price, signal, timestamp):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # Main sheet = trade log
    sheet = client.open("Algo_Trading_Log")

    try:
        trade_log = sheet.worksheet("Trade_Log")
    except:
        trade_log = sheet.add_worksheet(title="Trade_Log", rows="1000", cols="5")
    
    # Append signal row
    trade_log.append_row([timestamp, ticker, signal, price])
    print("✅ Logged to Trade_Log")

    # Simulated profit (for demo purposes only)
    simulated_sell_price = round(price * 1.03, 2)  # 3% gain
    pnl = round(simulated_sell_price - price, 2)
    is_win = int(pnl > 0)

    try:
        summary_sheet = sheet.worksheet("P&L_Summary")
    except:
        summary_sheet = sheet.add_worksheet(title="P&L_Summary", rows="1000", cols="5")

    summary_sheet.append_row([date, ticker, price, simulated_sell_price, pnl, "WIN" if is_win else "LOSS"])
    print(f"📈 P&L Summary: {ticker} - ₹{pnl:.2f} ({'WIN' if is_win else 'LOSS'})")
