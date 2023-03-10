
import datetime
from record import Record
import hkjc
import argparse

# -------------- 命令行傳入參數區 ---------------------------
parser = argparse.ArgumentParser(description='order hkjc marksix')
parser.add_argument('--order', action='store_true', default=False, help='order hkjc marksix')
parser.add_argument('--day', type=int, default=1, help="買入時是否計算天數")
parser.add_argument('--headless', action='store_true', default=False, help="顯示圖形")
args = parser.parse_args()



# -------------------- 下期攪珠日期 -------------------
record = Record()
next_draw_day = record.next_draw_info[1]
next_draw_id = record.next_draw_info[0]

day, month, year = next_draw_day[:2], next_draw_day[3:5], next_draw_day[6:10]
next_draw_day = datetime.date(int(year), int(month), int(day))
today = datetime.date.today()

# ---------------------------- 六合彩落注 ------------------------
if (today - next_draw_day).days == 0:
    hkjc.order(order=args.order, headless=args.headless)
else:
    print('離搞珠日還有:', today - next_draw_day)
    if args.day == 0:
        hkjc.order(order=args.order, headless=args.headless)