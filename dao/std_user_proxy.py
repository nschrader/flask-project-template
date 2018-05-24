from flask_login import current_user

class StdUserProxy:
    __std_user__ = None


    @classmethod
    def set(cls, user):
        cls.__std_user__ = user


    @classmethod
    def get(cls):
        if current_user:
            return current_user
        elif not cls.__std_user__:
            raise AttributeError("std_user not set")
        else:
            return cls.__std_user__
