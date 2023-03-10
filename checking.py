from record import Record
import json
import datetime
from gmailpy import Gmail
import config

# order_draw 己買的六合彩
try:
    with open('order.json', 'r') as f:
        order_draw = json.loads(f.read())
except FileNotFoundError:
    print('沒有找到order.json記錄')
    exit()

record = Record()
last_30_detail = record.last_30_detail
next_draw_day = record.next_draw_info[1]
next_draw_id = record.next_draw_info[0]
day, month, year = next_draw_day[:2], next_draw_day[3:5], next_draw_day[6:10]
next_draw_day = datetime.date(int(year), int(month), int(day))
today = datetime.date.today()

gmail = Gmail(config.gmail_login['username'], config.gmail_login['secret'])

def check(six):
    """在最後30期搞珠中核對號碼"""
    check_draw = []
    for draw in last_30_detail:
        if draw['id'] == six['id']:
            for n in six['no']:
                if n in draw['no']:
                  check_draw.append(n)
            gmail.sendCheck(f'{draw["id"]} 搞珠結果:{ draw["no"]}\n{six["id"]} 財運號碼: {six["no"]}\n{draw["id"]} 中奬號碼: {check_draw}')
            break # 這個break在這裡的作用是,己找到了對應的六合彩期數,己沒有必要再往下找.
    import os 
    os.remove('order.json')

if __name__=="__main__":
    check(order_draw)