import datetime
from record import Record
import hkjc
from marksix import markSix

record = Record()
next_draw_day = record.next_draw_info[1]
next_draw_id = record.next_draw_info[0]
# -------------------- 下期攪珠日期 ----------
day, month, year = next_draw_day[:2], next_draw_day[3:5], next_draw_day[6:10]
next_draw_day = datetime.date(int(year), int(month), int(day))
today = datetime.date.today()


if (today - next_draw_day).days == 0:
    six = markSix()
    hkjc.order(order=False)