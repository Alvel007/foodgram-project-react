from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import validate_username, validate_password


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    """
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=128,
        unique=True,
        blank=False,
        null=False,
        validators=[validate_username],
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=64,
        unique=True,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=128,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=128,
        blank=False,
        null=False,
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=64,
        blank=False,
        null=False,
        validators=[validate_password],
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """
    Информация о подписках.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'user'],
                name='unique_author_user',
            )
        ]

    def __str__(self):
        return f'{self.user.username} подписан на автора: '
        f'{self.author.username}'
