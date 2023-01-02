from django.urls import path
from .views import *


urlpatterns = [
    path('', message_list_view, name='message_list'),
]
