import smtplib
from email.message import EmailMessage

class Gmail():
    def __init__(self, username, secret) -> None:
        """usernaem: gmail user name
        secret: gmail 16-digit-app-password"""
        
        self.username = username
        self.secret = secret

    def send(self, msg: EmailMessage):
        
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.username, self.secret)
                smtp.send_message(msg)
                print('Complete!')
            except Exception as e:
                print(e)


    def sendCheck(self, content):
        message = EmailMessage()
        message['Subject'] = "MarkSix Checking"
        message['From'] = 'HKJC'
        message['To'] = 'hkcto.com@gmail.com'
        message.set_content(content)         
        self.send(message)
        print("marksix check email complete!")

    def sendOrder(self, content):
        message = EmailMessage()
        message['Subject'] = "MarkSix Order"
        message['From'] = 'HKJC'
        message['To'] = 'hkcto.com@gmail.com'
        message.set_content(content)         
        self.send(message)
        print("marksix order")
    
    def sendBalance(self, content):
        message = EmailMessage()
        message['Subject'] = "MarkSix Balance"
        message['From'] = 'pymarksix'
        message['To'] = 'hkcto.com@gmail.com'
        message.set_content(content)
        print(f'{content}')     



if __name__=="__main__":
    import config
    gmail = Gmail(username=config.gmail_login['username'], secret=config.gmail_login['secret'])
    # message = EmailMessage()
    # message['Subject'] = "MarkSix"
    # message['From'] = 'HKJC'
    # message['To'] = 'hkcto.com@gmail.com'
    # message.set_content(f'日期:\n財運號碼: \n結餘:')
    gmail.sendCheck('六合彩核對測試Email')  