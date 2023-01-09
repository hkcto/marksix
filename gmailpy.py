import smtplib
from email.message import EmailMessage

class Gmail():
    def __init__(self, username, secret) -> None:
        """usernaem: gmail user name
        secret: gmail 16-digit-app-password"""
        
        self.username = username
        self.secret = secret

    def send(self, msg: EmailMessage):
        """message = EmailMessage()\n
        message['Subject'] = "python Gmail"\n
        message['From'] = 'gmailpy'\n
        message['To'] = 'hkcto.com@gmail.com'\n
        message.set_content('gmail hello world')"""
        
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.username, self.secret)
                smtp.send_message(msg)
                print('Complete!')
            except Exception as e:
                print(e)
                

if __name__=="__main__":
    message = EmailMessage()
    message['Subject'] = "python Gmail"
    message['From'] = 'gmailpy'
    message['To'] = 'hkcto.com@gmail.com'
    message.set_content('gmail hello world')
    gmail = Gmail('hkcto.com@gmail.com')
    gmail.send(message)