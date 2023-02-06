import random
from record import Record


record = Record()
last_30_draw = record.last_30_draw

def rules(six):
    """財運號碼選擇規則"""

    # 3個號碼(七獎)以上,不能在最後30期結果中
    for draw in last_30_draw:
        three: list = []
        for i in six:
            if i in draw:
                three.append(i)
        if len(three) > 3:
            # print(three)
            return False
    # print('七獎PASS')
    
    #---------- six 是否同時有3種顏色 ----------
    redList = [1, 2, 7, 8, 12, 13, 18, 19, 23, 24, 29, 30, 34, 35, 40, 45, 46]
    # blueList = [3, 4, 9, 10, 14, 15, 20, 25, 26,31, 36, 37, 41, 42, 47, 48]
    greenList = [5, 6, 11, 16, 17, 21, 22, 27, 28, 32, 33, 38, 39, 43, 44, 49]
    red: list = []
    green: list = []
    blue: list = []
    for i in six:
        if i in redList:
            red.append(i)
        elif i in greenList:
            green.append(i)
        else:
            blue.append(i)
    # print(f"Red:{len(red)}\t Green:{len(green)}\t Blue:{len(blue)}")
    if len(red) and len(green) and len(blue) == 0:
        return False        
    # print('3顏色PASS')
    # -----------------------------------------------------
    
    # ----- 最後一個號碼不能小於30 -----
    if six[5] < 30:
        return False
    # print('最後號碼大於30,PASS')
    #------------------------------
    
    # ----- 沒有3個連續的號碼 ----------
    if six[2]-six[0] == 2:
        return False
    if six[3]-six[1] == 2:
        return False
    if six[4]-six[2] == 2:
        return False
    if six[5]-six[3] == 2:
        return False
    
    # -------------- 全部單數或偶數 --------------
    even, odd = [], [] #even為偶數,odd為奇數
    for i in six:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) | len(odd) == 0:
        return False
    # -------------------------------------------
    
    
    return six

def markSix():
    """隨機6位數字作為財運號碼,會經 rules()作過濾"""
    # 49 個數字
    fortyNine = [i+1 for i in range(49)]
    # six = sorted(random.sample(fortyNine, 6))
    six = False
    while not six:
        six = sorted(random.sample(fortyNine, 6))
        six = rules(six)
    return six
    
if __name__=="__main__":
    print(markSix())