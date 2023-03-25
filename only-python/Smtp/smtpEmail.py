import smtplib
from email.message import EmailMessage

Message = """
hello 
yes this is working

umesh Aku
"""

email = EmailMessage()

email['Subject'] = 'test email'
email['From'] = 'your_email@gmail.com'
email['To'] = 'umeshsaini8085@gmail.com'

email.set_content(Message)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('your_email@gmail.com', 'password')

smtp_connector.send_message(email)
smtp_connector.quit()
