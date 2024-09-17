import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv


load_dotenv() 



def send_email(**context):

    to_address = os.getenv("EMAIL_CONFIRMACION")
    host = os.getenv("SMTP_HOST")
    port = os.getenv("SMTP_PORT")
    subject = os.getenv("SMTP_SUBJECT")
    from_address = os.getenv("SMTP_MAIL_FROM")
    password = os.getenv("SMTP_PASSWORD")

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Create HTML content
    html_content = f"""
    <html>
    <body>
        <p>Extracción de datos desde API y carga a Redshift a sido exitosa.</p>
    </body>
    </html>
    """

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Create an SMTP session
        server = smtplib.SMTP(host, port)  # Use your SMTP server and port
        server.starttls()  # Enable security

        # Login to the server
        server.login(from_address, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")