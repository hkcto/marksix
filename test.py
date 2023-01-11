from record import Record
from marksix import markSix
import json
draw_info = Record().next_draw_info
with open('order.json', 'w', encoding='utf-8') as f:
    order_draw = {"id": draw_info[0], "date": draw_info[1], "no": markSix()}
    f.write(json.dumps(order_draw))
    
