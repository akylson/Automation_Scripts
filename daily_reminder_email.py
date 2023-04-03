import schedule
import time
from send_email import send_email  # Import the send_email function from the previous example

def daily_email_reminder():
    subject = "Daily Reminder"
    body = "This is your daily reminder to stay productive!"
    to_email = "recipient@example.com"
    from_email = "sender@example.com"
    smtp_server = "smtp.example.com"
    password = "your_password"

    send_email(subject, body, to_email, from_email, smtp_server, password)
    print("Daily reminder email sent!")

# Schedule the daily email reminder
schedule.every().day.at("08:00").do(daily_email_reminder)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check for pending tasks every minute