import os
import imghdr
from email.message import EmailMessage
import smtplib


class SendingMail():
    @staticmethod
    def mail():

        EMAIL_ADDRESS = 'jain.22apurv@gmail.com'
        EMAIL_PASS = os.environ.get('GMAIL_APP_KEY')

        msg = EmailMessage()
        msg['Subject'] = "This is a test mail with an attachment"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'jain.11apurv@gmail.com'
        msg.set_content(
            'This email has been sent for testing purpose and it sent via Python. The mail also contains an attachment')

        with open('Bar_chart.png', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            try:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
                print("sending your mail...")
                smtp.send_message(msg)
                print("Mail has been sent successfully")
            except Exception as e:
                print("Exception occurred sending your mail" + str(e))