from flask import current_app as app
from mail import send_to

@app.route("/sendMailTo/<to>")
def testMail(to):
    send_to([to], "Test", "This is a test")
    return "done"
