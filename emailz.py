#!/anaconda3/bin/python

import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

FEMAIL = 'muellerm111@frontier.com'

# Create the base text message.
msg = EmailMessage()
msg['Subject'] = "Printheads"
msg['From'] = Address("Mike Mueller", "muellerm111", "frontier.com")
msg['To'] = (Address("Muellers", "m2", "themuellers.us"),
             Address("beach 5520", "88b34hjm", "hpeprint.com"))


msg.set_content('...........')  # Not at all sure what this does
# Add the html version.  This converts the message into a multipart/alternative
# container, with the original text message as the first part and the new html
# message as the second part.
colors_cid = make_msgid()
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Hello printer!</p>
    <p>I have a nice color pattern to help clean your printheads.</br>
    This should keep you healthy.</p>
    <img src="cid:{colors_cid}" />
  </body>
</html>
""".format(colors_cid=colors_cid[1:-1]), subtype='html')
# note that we needed to peel the <> off the msgid for use in the html.

# Now add the related image to the html part.
with open("pcolors.png", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid=colors_cid)

# Make a local copy of what we are going to send.
# with open('outgoing.msg', 'wb') as f:
#     f.write(bytes(msg))

# Send the message via preferred SMTP server.
with smtplib.SMTP(host='smtp.frontier.com', port=587) as conn:
    print(conn.ehlo())
    # print(conn.starttls())
    print(conn.login(FEMAIL, 'Pa88.4.Fm'))
    print(conn.send_message(msg))

