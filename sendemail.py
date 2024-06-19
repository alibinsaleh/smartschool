import smtplib
from email.message import EmailMessage
import os

def send_email_with_attachment(smtp_server, port, sender_email, sender_password, recipient_email, subject, body, attachment_path):
    # Create the email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Add the attachment
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Example usage
smtp_server = 'smtp.gmail.com'
port = 465
sender_email = 'alibinsaleh@gmail.com'
sender_password = 'gznj osoa phee tgoe'
recipient_email = 'alibinsaleh@gmail.com'
subject = 'Subject of the Email'
body = 'This is the body of the email'
attachment_path = 'students_data.csv'

send_email_with_attachment(smtp_server, port, sender_email, sender_password, recipient_email, subject, body, attachment_path)

