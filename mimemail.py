import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename


def send_mail(send_from: str, subject: str, text: str,
              send_to: list, files=None):

    send_to = default_address if not send_to else send_to

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype=ext)
            attachedfile.add_header('Content-ID', '<pdf1>')
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(f))
            attachedfile.add_header(
                'content-disposition', 'inline', filename=basename(f))
        msg.attach(attachedfile)

    smtp = smtplib.SMTP(host='smtp.frontier.com', port=587)
    print(smtp.ehlo())
    # print(smtp.starttls())
    print(smtp.login(username, password))
    print(smtp.sendmail(send_from, send_to, msg.as_string()))
    smtp.close()


username = 'muellerm111@frontier.com'
password = 'Pa88.4.Fm'
mail_to = 'mikemu1@comcast.net'
message = '''
This is only the start of things to come.
Look for more later today.
'''


send_mail(send_from=username,
          subject="MIME test 2",
          text=message,
          send_to=None,
          files=['./Colors.pdf']
          )
