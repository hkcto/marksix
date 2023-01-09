from playwright.sync_api import Playwright, sync_playwright, expect
import config
from marksix import markSix


def run(playwright: Playwright, marksix: list, order=False) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bet.hkjc.com/marksix/Single.aspx?lang=ch")
    
    # ------------------------ 登入HKJC: Account and Password --------------------------
    page.locator('//*[@id="account"]').click() #登入名稱輸入框
    page.locator('//*[@id="account"]').fill(config.hkjc['username']) #輸入用戶名
    page.locator('//*[@id="passwordInput1"]').type(config.hkjc['password']) # 輸入密碼
    page.locator('//*[@id="loginButton"]').click() # 登入button
    # ------------登入HKJC: 回答問題 -----------------
    page.wait_for_selector('//*[@id="ekbaSeqQuestion"]', strict=True)
    question = page.locator('//*[@id="ekbaSeqQuestion"]').text_content() #登入 Question
    print("Question:", question)
    ask = config.hkjc[f'{question}']
    print("ask:", ask)
    page.locator('//*[@id="ekbaDivInput"]').type(ask)
    page.locator('//*[@id="pic_confirm"]').click() # ask button
    page.locator('//*[@id="disclaimerProceed"]').click() #條款及細則page
    
    # ---------- 結餘 ----------
    balance = page.locator('//*[@id="valueAccBal"]').all_text_contents()[0]
    print(balance)
    balance = float(balance[6:])
    if balance < 10:    # 結餘小於$10就退出
        page.close()
        browser.close()
    
    
    # ----- 選擇財運號碼 -----
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
        # --------------------- send email ----------------------
        
        from gmailpy import Gmail
        from email.message import EmailMessage
        from datetime import datetime
        gmail = Gmail(username=config.gmail_login['username'], secret=config.gmail_login['secret'])
        message = EmailMessage()
        message['Subject'] = "MarkSix"
        message['From'] = 'HKJC'
        message['To'] = 'hkcto.com@gmail.com'
        message.set_content(f'日期: {datetime.today()}\n財運號碼: {marksix}\n結餘: {balance}')
        gmail.send(message)   
    else:
        print('just test mode')
    
    
    # page.pause()
    # ---------------------
    context.close()
    browser.close()

def order(order=False):
    with sync_playwright() as playwright:
        run(playwright, marksix=markSix(), order=order)

if __name__=='__main__':
    
    with sync_playwright() as playwright:
        run(playwright, marksix=markSix())