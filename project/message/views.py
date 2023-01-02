from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import QueryDict
from django.http import HttpResponseRedirect


def message_list_view(request):

    if request.method == 'POST':
        post_dictionary = request.POST.copy()
        form = MessageForm(post_dictionary)
        if form.is_valid():
            print('\nСоздаётся новое сообщение!\n')
            Message.objects.create(author=request.user, text=request.POST['text'])
            return redirect('/')
            #new_message = Message.objects.create(author=request.user, text=request.POST['text'])

    form = MessageForm()

    objects = Message.objects.all().order_by('-sent_time')
    return render(request, 'message_list.html', context={'objects': objects, 'user': request.user, 'form': form})
