from flask_mail import Message

from extensions import mail

def send_to(recipients, title, content):
    msg = Message(title, recipients=recipients)
    msg.body = content
    mail.send(msg)
