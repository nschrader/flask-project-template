from flask_mail import Message
from flask import redirect, url_for, render_template, Markup

from extensions import mail

def send_confirmation_to(utilisateur, host_url):
    utilisateur.make_token()
    utilisateur.save()

    url = host_url[:-1] + url_for("inscription_token", token = utilisateur.token)

    msg = Message("Confirmation inscription", recipients=[utilisateur.mail])
    msg.html = Markup(render_template('mail.html',url=url))
    mail.send(msg)

    return redirect(url_for('login', token = utilisateur.token))
