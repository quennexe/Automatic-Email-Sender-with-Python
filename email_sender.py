

import smtplib
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email(to_list, subject, body):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(to_list)  
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ E-posta başarıyla gönderildi!")
    except Exception as e:
        print("❌ E-posta gönderilemedi:", e)
