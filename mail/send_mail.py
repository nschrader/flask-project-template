from flask_mail import Message

from extensions import mail

def send_to(recipient, title, content):
    msg = Message(title, recipients=[recipient])
    msg.html = content
    mail.send(msg)
