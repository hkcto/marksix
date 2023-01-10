import datetime
from record import Record
import hkjc
import argparse
import os

# ----------------- 調整python工作目錄--------------
os.chdir(os.getcwd())

# -------------- 命令行傳入參數區 ---------------------------
parser = argparse.ArgumentParser(description='order hkjc marksix')
parser.add_argument('--order', action='store_true', help='order hkjc marksix')
args = parser.parse_args()


record = Record()
next_draw_day = record.next_draw_info[1]
next_draw_id = record.next_draw_info[0]
# -------------------- 下期攪珠日期 -------------------
day, month, year = next_draw_day[:2], next_draw_day[3:5], next_draw_day[6:10]
next_draw_day = datetime.date(int(year), int(month), int(day))
today = datetime.date.today()

# ---------------------------- 核對中奬號嗎 ------------------------

if (today - next_draw_day).days == 0:
    hkjc.order(order=args.order)
else:
    print('離搞珠日還有:', today - next_draw_day)