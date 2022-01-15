import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from dotenv import load_dotenv

def send_email(mail_content:str):
    load_dotenv()
    
    context = ssl.create_default_context()
    content_mail = mail_content

    sender_address = environ.get('SENDER_EMAIL_ADDRESS')
    sender_password = environ.get('SENDER_EMAIL_PASSWORD')

    mail_subject = "Feedback from the user"
    receiver_address = "ashishsarmah11@gmail.com"

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = mail_subject
    message.attach(MIMEText(content_mail, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            try:
                server.login(sender_address, sender_password)
                text = message.as_string()
                try:
                    server.sendmail(sender_address, receiver_address, text)
                    server.quit()

                except Exception as e:
                    print("Mail Send Failed")
                    print(e)
            
            except smtplib.SMTPAuthenticationError:
                print("Authentication Error")

    except Exception:
        print("Error: unable to send email")
