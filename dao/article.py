from datetime import datetime
from flask import Markup
from mongoengine import *

from extensions import markdown
from .audit import Audit

class Article(Audit, EmbeddedDocument):
    text = StringField(required = True)


    @staticmethod
    def get_markup_for(article):
        if article:
            return Markup(markdown(article.text))
        else:
            return Markup(markdown("Soyez le premier à rediger un avis"))

    @staticmethod
    def get_article_text(article):
        if article:
            return article.text
        else:
            return "Soyez le premier à rediger un avis"
