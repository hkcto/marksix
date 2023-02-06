# last30draw
# https://bet.hkjc.com/contentserver/jcbw/cmc/last30draw.json
# start page https://bet.hkjc.com/marksix/index.aspx?lang=ch
#

import json
import httpx
import re

class Record():
    def __init__(self) -> None:
        self.last_30_draw, self.last_30_detail = last30draw()
        self.next_draw_info = nextDrawInfo()
        # self.last_draw = lastDrawDetail()

def last30draw():
    """更新六合彩結果到draw.json檔案中,返回 last30draw list"""
    
    r = httpx.get(url="https://bet.hkjc.com/contentserver/jcbw/cmc/last30draw.json").json()
    
    # ----- 保存last30draw.json ----------
    for i in range(len(r)):
        draw = r[i]['no']
        r[i]['no'] = list(map(int, draw.split('+')))
    with open("draw.json", 'w', encoding='utf8') as f:
        json.dump(r, f, ensure_ascii=False ,indent=1)
 
    #返回 last30draw list
    return [i['no'] for i in r], r
   
def nextDrawInfo():
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
    with httpx.Client(headers=header) as client:
        single_page = client.post('https://bet.hkjc.com/marksix/Single.aspx?lang=ch').text
    draw = re.search('[0-9][0-9]/[0-9][0-9][0-9]', single_page)
    date = re.search('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]', single_page)
    return [draw.group(0), date.group(0)]

if __name__=="__main__":

    record = Record()
    # print(record.last_30_draw)
    # print(lastDrawDetail())
    print(record.last_30_detail)
    