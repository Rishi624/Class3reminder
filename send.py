import smtplib
from email.mime.text import MIMEText
import schedule
import time
import datetime

def send_email(subject, body):
    sender_email = "waste4159@gmail.com"  # The email that sends the data
    sender_password = "jupe umix nfqa xkcp"  # The sender's password or app password
    receiver_email = "rishiyelamarthy12345@gmail.com"  # The email that receives the data.
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Change if not Gmail.
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent!")
    except Exception as e:
        print(f"Error: {e}")

def daily_notification():
    today = datetime.datetime.now().weekday()  # 0 = Monday, 1 = Tuesday, etc.
    messages = {
        0: {"subject": "Monday Class Info", "body": "Python:320\nMath:307\nDLC:202A\nPhysics practical:111"},
        1: {"subject": "Tuesday Class Info", "body": "Math:307\nFEEE:207\nPhysics:404\nDLC:202A\nEnglish:317"},
        2: {"subject": "Wednesday Class Info", "body": "Math:211\nPhysics:404\nEntrepreneurship:408\nFEEE:310\nPython:320"},
        3: {"subject": "Thursday Class Info", "body": "Physics:409\nEntrepreneurship:202A\nFEEE practical:CB\nMath:207\nConstitution:405"},
        4: {"subject": "Friday Class Info", "body": "English:317\nPython:314\nFEEE:311"},
        5: {"subject": "Saturday Class Info", "body": "Enjoy the day"},
        6: {"subject": "Sunday Class Info", "body": "Enjoy the day"},
    }

    if today in messages:
        send_email(messages[today]["subject"], messages[today]["body"])
    else:
        print("Invalid day.")

schedule.every().day.at("07:16").do(daily_notification)  # Change the time as needed.

while True:
    schedule.run_pending()
    time.sleep(1)