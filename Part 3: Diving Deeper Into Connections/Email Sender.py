import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
sender_email = "<your email>"  # Your email
sender_password = "<your app password>"  # Your email password
recipient_email = "<a recipient email>"  # Recipient's email

# Create the server connection
smtp_server = "smtp.gmail.com"  # For Gmail
smtp_port = 587  # TLS port

# Email sending loop (e.g., for debugging or testing consented bulk messages)
for i in range(3):  # Replace with the desired count
    try:
        # Create an email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = f"Test Email #{i+1}"

        # Body of the email
        body = f"This is a test email #{i+1}."
        message.attach(MIMEText(body, "plain"))

        # Set up the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"Email #{i+1} sent successfully.")

    except Exception as e:
        print(f"Failed to send email #{i+1}: {e}")
