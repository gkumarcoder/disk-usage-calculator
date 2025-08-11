import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "alert@yourdomain.com"
    msg['To'] = to_email

    with smtplib.SMTP('smtp.yourmailserver.com', 587) as server:
        server.starttls()
        server.login("username", "password")
        server.send_message(msg)

send_email_alert("🚨 Disk Alert", "Disk usage exceeded 90%!", "admin@example.com")
