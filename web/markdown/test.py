from flask import Markup, current_app as app
from markdown import markdown

@app.route('/markdown')
def markdownTest():
  content = """
Chapter
=======

Section
-------

* Item 1
* Item 2
"""
  return Markup("<html>" + markdown(content) + "</html>")
