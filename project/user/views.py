from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupUserForm
from .models import *


class SignUp(CreateView):
    form_class = SignupUserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
