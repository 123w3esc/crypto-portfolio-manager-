from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL")
SENDER_PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER")


def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Email failed:", e)


def check_alerts(metrics):

    for coin in metrics.index:

        avg_return = metrics.loc[coin, "avg_daily_return"]
        volatility = metrics.loc[coin, "volatility"]

        if avg_return > 0.02:
            subject = f"🚀 High Return Alert: {coin}"
            body = f"{coin} average daily return is high.\nReturn: {avg_return:.4f}"
            send_email(subject, body)

        if volatility > 0.06:
            subject = f"⚠ High Risk Alert: {coin}"
            body = f"{coin} volatility is high.\nVolatility: {volatility:.4f}"
            send_email(subject, body)
def send_report_link(file):

    subject = "Crypto Portfolio Report"
    body = f"Your report is generated.\nDownload here: {file}"

    send_email(subject, body)