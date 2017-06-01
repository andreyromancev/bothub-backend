from django.contrib import admin
from service.authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email')

admin.site.register(User, UserAdmin)
