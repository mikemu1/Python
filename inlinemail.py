import cgi
import uuid
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

username = 'muellerm111@frontier.com'
password = 'Pa88.4.Fm'
mail_to = 'mikemu1@comcast.net'
subj = 'MIME inline 3'
message = '''
This is only the start of things to come.
Look for more later today.
'''

img = dict(title=u'Picture report…',
           path=u'Colors.png', cid=str(uuid.uuid4()))

msg = MIMEMultipart('related')
msg['Subject'] = Header(subj, 'utf-8')
msg['From'] = username
msg['To'] = mail_to
msg_alternative = MIMEMultipart('alternative')
msg.attach(msg_alternative)


msg_text = MIMEText(u'\n\nnow is the time', 'plain', 'utf-8')
# msg_text = MIMEText(u'Who knows'.format(**img), 'plain', 'utf-8')
msg_alternative.attach(msg_text)
'''
msg_html = MIMEText(u'<div dir="ltr">'
                    '<img src="cid:{cid}" alt="{alt}"><br></div>'
                    .format(alt=cgi.escape(img['title'], quote=True), **img),
                    'html', 'utf-8')
msg_alternative.attach(msg_html)
'''
with open(img['path'], 'rb') as file:
    msg_image = MIMEImage(file.read(), name=os.path.basename(img['path']))
    msg.attach(msg_image)
msg_image.add_header('Content-ID', '<{}>'.format(img['cid']))


smtp = smtplib.SMTP(host='smtp.frontier.com', port=587)
print(smtp.ehlo())
# print(smtp.starttls())
print(smtp.login(username, password))
print(smtp.sendmail(username, mail_to, msg.as_string()))
smtp.close()
