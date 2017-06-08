import re
from django.db.models import SmallIntegerField
from django.core.exceptions import ValidationError


class InvalidConstantFieldNameException(Exception):
    pass


class ConstantField(SmallIntegerField):
    def __init__(self, constant=None, **kwargs):
        kwargs.setdefault('validators', []).append(self._validate)
        if 'choices' not in kwargs:
            kwargs['choices'] = constant.get_choices()

        super(ConstantField, self).__init__(**kwargs)
        self._constant = constant

    def contribute_to_class(self, cls, name):
        super(ConstantField, self).contribute_to_class(cls, name)

        if not self.attname.endswith('_id'):
            raise InvalidConstantFieldNameException

        def constant_getter(model_obj):
            value = getattr(model_obj, self.attname)

            return self._constant.get_name(value)

        def constant_setter(model_obj, value):
            const_id = self._constant.get_id(value)
            if const_id is None:
                raise ValidationError('Wrong constant value')

            setattr(model_obj, self.name, const_id)

        setattr(cls, re.sub(r'^(.*)_id$', r'\1', self.name), property(constant_getter, constant_setter))

    def _validate(self, value):
        if not self._constant.get_name(value):
            raise ValidationError('Wrong constant value')
