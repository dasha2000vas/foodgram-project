from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import value_validator


class User(AbstractUser):
    unicode_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. Letters, digits and @/./+/-/_ only.'),
        validators=[unicode_validator, value_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'),
        max_length=254,
        unique=True,
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
    first_name = models.CharField(
        _('first name'),
        max_length=150,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        db_table = 'auth_user'

    def __str__(self):
        return self.username
