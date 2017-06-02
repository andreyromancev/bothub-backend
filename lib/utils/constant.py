class Constant:
    @classmethod
    def get_choices(cls):
        return tuple((k, v) for k, v in cls.__dict__.items() if k.isupper())

    @classmethod
    def get_name(cls, const_id):
        for k, v in cls.__dict__.items():
            if k.isupper() and v == const_id:
                return k.lower()

        return None

    @classmethod
    def get_id(cls, name):
        return getattr(cls, name.upper(), None)
