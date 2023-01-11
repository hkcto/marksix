from record import Record
import json

record = Record()
last_30_detail = record.last_30_detail

# order_draw 己買的六合彩
with open('order.json', 'r') as f:
    order_draw = json.loads(f.readline())
    
def check(six):
    """在最後30期搞珠中核對號碼"""
    check_draw = []
    for draw in last_30_detail:
        if draw['id'] == six['id']:

            for n in six['no']:
                if n in draw['no']:
                  check_draw.append(n)
            print(f'{draw["id"]} 搞珠結果:', draw['no'])
            print(f'{six["id"]} 財運號碼:', six['no'])
            print(f"{draw['id']} 中奬號碼:",check_draw)
            break
        else:
            print('沒有中')
    return check_draw
if __name__=="__main__":
    check(order_draw)