import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError('Недопустимое значение поля!')
    if not bool(re.match(r'^[\w.@+-]+$', value)):
        raise ValidationError('Некорректные символы в username')
    return value


def validate_password(value):
    if not re.search(r'\d', value):
        raise ValidationError('Пароль должен содержать хотя бы одну цифру')

    if not re.search(r'^[\w.@+-]+$', value):
        raise ValidationError('Пароль должен содержать '
                              'хотя бы один специальный символ')

    if not re.search(r'[a-z]', value):
        raise ValidationError('Пароль должен содержать '
                              'хотя бы одну строчную букву')

    if not re.search(r'[A-Z]', value):
        raise ValidationError('Пароль должен содержать '
                              'хотя бы одну заглавную букву')
