import smtplib

from email.message import EmailMessage


email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'mikemu1@comcast.net'
email['To'] = 'mikemu1@comcast.net'
email['Cc'] = ['m2@themuellers.us', 'mikemu0919@me.com']

email_content = """Hello Mike,

Message goes here.

"""

email.set_content(email_content)

conn = smtplib.SMTP(host='smtp.comcast.net', port=587)

print('\n')
resp = conn.ehlo()
print(f'{resp}\n')

resp = conn.starttls()
print(f'{resp}\n')


resp = conn.login('mikemu1@comcast.net', 'omitbgf')
print(f'{resp}\n')

resp = conn.send_message(email)
print(f'{resp}\n')

conn.quit()
