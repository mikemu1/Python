import smtplib

from email.message import EmailMessage

FEMAIL = 'muellerm111@frontier.com'
email = EmailMessage()

email['Subject'] = 'Frontier email'
email['From'] = FEMAIL
email['To'] = 'mikemu1@comcast.net'
email['Cc'] = 'mikemu0919@me.com'

email_content = """Hello Mike,

Message goes here.

"""

email.set_content(email_content)

conn = smtplib.SMTP(host='smtp.frontier.com', port=587)

print('\n')
resp = conn.ehlo()
print(f'{resp}\n')

# resp = conn.starttls()
# print(f'{resp}\n')


resp = conn.login(FEMAIL, 'Pa88.4.Fm')
print(f'{resp}\n')

resp = conn.send_message(email)
print(f'{resp}\n')

conn.quit()
