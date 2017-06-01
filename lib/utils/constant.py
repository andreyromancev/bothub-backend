class Constant:
    def __init__(self, **kwargs):
        choices = list()
        self._values = dict()
        for k, v in kwargs.items():
            self._values[k] = v
            choices.append((v, k))

        self.CHOICES = tuple(choices)

    def __getattr__(self, attname):
        try:
            return self._values[attname]
        except KeyError:
            raise AttributeError(attname)

    def get_name(self, const_id):
        for k, v in self._values.items():
            if v == const_id:
                return k

        return None

    def get_id(self, const_name):
        return getattr(self, const_name, None)
