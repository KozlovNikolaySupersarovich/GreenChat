from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import QueryDict
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.base import TemplateView


def message_list_view(request):
    print(request)
    form = MessageForm()

    objects = Message.objects.all().order_by('-sent_time')
    request.session['last_message'] = objects.all().first().pk
    return render(request, 'message_list.html', context={'objects': objects, 'user': request.user, 'form': form})


def message_send(request):
    field = request.GET.get('text')
    print(request.GET)
    print(request.POST)
    form = MessageForm(request.GET)
    if form.is_valid():
        print('\nСоздаётся новое сообщение!\n')
        Message.objects.create(author=request.user, text=request.GET['text'])
    answer = 'You typed: ' + field

    data = {
        'respond': answer
            }
    return JsonResponse(data)


def message_get(request):
    last_seen_message = request.session['last_message']
    last_registered_message = Message.objects.all().last().pk
    messages_to_get = []
    for i in range(last_seen_message, last_registered_message):
        m = Message.objects.get(pk=i+1)
        temp_message = {
            'author': m.author.username,
            'text': m.text,
            'sent_time': m.sent_time,
            'author_status': m.author.status,
        }
        messages_to_get.append(temp_message)

    print(messages_to_get)
    data = {
        'messages_to_get': messages_to_get
    }
    request.session['last_message'] = last_registered_message
    return JsonResponse(data)


class IndexView(TemplateView):
    template_name = 'index.html'


def answer_search(text):
    pass
