from django.contrib import admin
from service.market.models import BotProfile


class BotProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)

admin.site.register(BotProfile, BotProfileAdmin)
