from flask import current_app as app
from flask import render_template,Markup
from mail import send_to

@app.route("/sendMailTo/<to>")
def testMail(to,url):
    send_to(to, "Test", Markup(render_template('misc/mail.html',url=url)))
    return "done"
