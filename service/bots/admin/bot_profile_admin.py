from django.contrib import admin
from ..models import BotProfile


class BotProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)

admin.site.register(BotProfile, BotProfileAdmin)
