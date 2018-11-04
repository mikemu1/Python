import smtplib

from email.message import EmailMessage


email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'mikemu0919@gmail.com'
email['To'] = 'mikemu1@comcast.net'
email['Cc'] = 'm2@themuellers.us'

email_content = """Hello Mike,

Nonsense goes here.

"""

email.set_content(email_content)

conn = smtplib.SMTP(host='smtp.gmail.com', port=587)

print('\n')
resp = conn.ehlo()
print(f'{resp}\n')

resp = conn.starttls()
print(f'{resp}\n')


resp = conn.login('mikemu0919@gmail.com', 'ylxnkmrpbubkkxvt')
print(f'{resp}\n')

resp = conn.send_message(email)
print(f'{resp}\n')

conn.quit()
