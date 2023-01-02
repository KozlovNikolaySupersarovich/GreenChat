from django.contrib import admin
from .models import *


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['author', 'text', 'sent_time']


admin.site.register(Message, MessageAdmin)
