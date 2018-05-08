from flask import current_app as app
from flask_mail import Message

from ..extensions import mail

def send_to(recipients, title, content):
    msg = Message(title, recipients=recipients)
    msg.body = content
    mail.send(msg)

@app.route("/sendMailTo/<to>")
def testMail(to):
    send_to([to], "Test", "This is a test")
    return "done"
