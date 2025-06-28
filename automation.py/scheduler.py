# automation/scheduler.py
import schedule
import time
from main import main

def run_schedule():
    schedule.every().day.at("09:30").do(main)
    while True:
        schedule.run_pending()
        time.sleep(60)
