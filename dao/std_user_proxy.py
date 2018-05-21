class StdUserProxy:
    __std_user__ = None

    @classmethod
    def set(cls, user):
        cls.__std_user__ = user

    @classmethod
    def get(cls):
        if not cls.__std_user__:
            raise AttributeError("std_user not set")
        else:
            return cls.__std_user__
