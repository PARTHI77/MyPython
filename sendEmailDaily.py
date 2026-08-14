'''
Explanation

Email Configuration:-

sender_email, receiver_email, and password: Replace these with your actual email credentials.

smtp.example.com: Replace with your email provider's SMTP server (e.g., smtp.gmail.com for Gmail).

Creating the Email:-

MIMEMultipart(): Creates a multipart message.
MIMEText(body, 'plain'): Adds a plain text body to the email.

Connecting to the SMTP Server:-

smtplib.SMTP('smtp.example.com', 587): Connect to the SMTP server.
starttls(): Secure the connection.
login(sender_email, password): Log in to the SMTP server.
sendmail(sender_email, receiver_email, text): Send the email.

Scheduling:-

schedule.every().day.at("08:00").do(send_email): Schedule send_email to run every day at 08:00.
while True: Keeps the script running to check for scheduled tasks.

Notes:-

Email Provider Settings:-
Some email providers (like Gmail) require you to enable "Less secure app access" or use an app-specific password.

Testing:
Before deploying, test the script by sending an email to yourself to ensure everything is set up correctly.

Security:
Never hard-code passwords in your scripts. Consider using environment variables or a configuration file with appropriate permissions.

With this setup, your script will automatically send a daily email report at the specified time.
'''

import smtplib
import time
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    # Email configuration
    sender_email = "iamponniyinselvan@gmail.com"
    receiver_email = "parthiban.paul@gmail.com"
    password = "$password"

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Daily Report"

    # Email body
    body = "This is your daily report sent for Python testing."
    msg.attach(MIMEText(body, "plain"))

    # Connect to Gmail and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(
                sender_email,
                receiver_email,
                msg.as_string()
            )

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")


def schedule_email():
    # Run every day at 08:00
    schedule.every().day.at("22:06").do(send_email)

    print("Email scheduler started. Waiting for 22:06...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_email()
