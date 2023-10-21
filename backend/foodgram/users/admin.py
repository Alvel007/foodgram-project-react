from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from foodgram.settings import EMPTY_VALUE_DISPLAY
from users.models import Follow, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username')
    search_fields = ('username', 'email')
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('author', 'user',)
    search_fields = (
        'author__username',
        'author__email',
        'user__username',
        'user__email',
    )
    empty_value_display = EMPTY_VALUE_DISPLAY
