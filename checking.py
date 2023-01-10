from record import Record
import json

record = Record()
last_30_detail = record.last_30_detail

# order_draw 己買的六合彩
with open('order.json', 'r') as f:
    order_draw = json.loads(f.readline())
    
def check(six):
    for draw in last_30_detail:
        if draw['id'] == six['id']:
            print(draw['no'], six['no'])
            break
    else:
        print('沒有中')
        
if __name__=="__main__":
    check(order_draw)