from playwright.sync_api import Playwright, sync_playwright
import config
from marksix import markSix
from gmailpy import Gmail



def run(playwright: Playwright, marksix: list, order=False, headless=True) -> None:
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bet.hkjc.com/marksix/Single.aspx?lang=ch")
    
    # ------------------------ 登入HKJC: Account and Password --------------------------
    page.locator('//*[@id="account"]').click() #登入名稱輸入框
    page.locator('//*[@id="account"]').fill(config.hkjc['username']) #輸入用戶名
    page.locator('//*[@id="passwordInput1"]').type(config.hkjc['password']) # 輸入密碼
    page.locator('//*[@id="loginButton"]').click() # 登入button
    # ------------登入HKJC: 回答問題 -----------------
    # page.wait_for_selector('//*[@id="ekbaSeqQuestion"]', strict=True)
    question = page.locator('//*[@id="ekbaSeqQuestion"]').text_content() #登入 Question
    print("Question:", question)
    ask = config.hkjc[f'{question}']
    print("ask:", ask)
    page.locator('//*[@id="ekbaDivInput"]').type(ask)
    page.locator('//*[@id="pic_confirm"]').click() # ask button
    page.locator('//*[@id="disclaimerProceed"]').click() #條款及細則page
    
    
    # ----------------------- Email ----------------------------
    gmail = Gmail(username=config.gmail_login['username'], secret=config.gmail_login['secret'])
    
    # ---------- 結餘 ----------
    balance_text = page.locator('//*[@id="valueAccBal"]').all_text_contents()[0]
    print(balance_text)
    balance = float(balance_text[6:])
    if balance < 10:    # 結餘小於$10就退出
        gmail.sendBalance(balance_text)
        page.close()
        browser.close()
    
    
    # ------------------------------------- 選擇財運號碼 ---------------------------
    for i in marksix:
        page.click(selector=f'//*[@id="n{i}"]')

    # ----- 加入注項和傳送注項 -----
    # 加入注項 button
    page.click('//*[@id="oddsTable"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[6]/td/table/tbody/tr[3]/td/div[1]')
    page.click('//*[@id="bsSendPreviewButton"]') # 傳送注項 button
    if order:
        page.click('//*[@id="previewSend"]') # 確定傳送 buttuon
        page.click('//*[@id="replyClose"]') #完成 buttuon
        print('己成功購買:', marksix)
        
        # ------------------------ 下期攪珠資訊 -----------------------
        from record import Record
        draw_info = Record().next_draw_info
        
        # --------------------- send email ----------------------

        balance = page.locator('//*[@id="valueAccBal"]').all_text_contents()[0]
        gmail = Gmail(username=config.gmail_login['username'], secret=config.gmail_login['secret'])
        gmail.sendOrder(f'期數: {draw_info[0]}\n日期: {draw_info[1]}\n財運號碼: {marksix}\n結餘: {balance}')
        
        # ------------ order log -----------------------
        from record import Record
        import json
        draw_info = Record().next_draw_info
        with open('order.json', 'w', encoding='utf-8') as f:
            order_draw = {"id": draw_info[0], "date": draw_info[1], "no": marksix}
            f.write(json.dumps(order_draw))
    else:
        print('Test Model')
        page.pause()
    
    # page.pause()
    # ---------------------
    context.close()
    browser.close()

def order(order=False, headless=True):
    # 這個函數是為了給 run.py 調用
    with sync_playwright() as playwright:
        run(playwright, marksix=markSix(), order=order, headless=headless)

if __name__=='__main__':
    
    with sync_playwright() as playwright:
        run(playwright, marksix=markSix(),order=False, headless=False)