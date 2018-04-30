import re
from flask_wtf import Form

from wtforms.fields import TextField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import url, length, regexp, optional


class SettingsForm(Form):
    """docstring for SettingsForm"""

    ui_lang = SelectField(
        label="Primary site language",
        description="Site will try to show UI labels using this " +
            "language. User data will be shown in original languages.",
    )
    url = URLField(
        label="Personal site URL",
        description="If you have personal site and want to share " +
            "with other people, please fill this field",
        validators=[optional(), url(message="Invalid URL.")])
    username = TextField(
        label="Public profile address",
        description="Will be part of your public profile URL. Can " +
            "be from 2 up to 40 characters length, can start start from [a-z] " +
            "and contains only latin [0-9a-zA-Z] chars.",
        validators=[
            length(2, 40, message="Field must be between 2 and 40" +
            " characters long."),
            regexp(r"[a-zA-Z]{1}[0-9a-zA-Z]*",
                re.IGNORECASE,
                message="Username should start from [a-z] and " +
                    "contains only latin [0-9a-zA-Z] chars")
        ]
    )
