import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email=None):
    host = os.getenv('EMAIL_HOST')
    port = int(os.getenv('EMAIL_PORT', 587))
    user = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASSWORD')
    to_email = to_email or os.getenv('EMAIL_TO')

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

if __name__ == '__main__':
    send_email('Test Subject', '<h1>Hello World</h1>') 