# utils/helpers.py

from datetime import datetime

def format_date(dt):
    if isinstance(dt, datetime):
        return dt.strftime("%Y-%m-%d")
    return str(dt)

def format_currency(value):
    return f"₹{value:,.2f}"

def calculate_percentage_change(old, new):
    if old == 0:
        return 0
    return round(((new - old) / old) * 100, 2)
