from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('message_send/', message_send, name='message_send'),
    path('message_get/', message_get, name='message_get'),
    path('messages/', message_list_view, name='message_list'),
]
