from django import forms
from .models import *


class MessageForm(forms.Form):
    text = forms.CharField(label='',
                           widget=forms.Textarea(attrs={'maxlength': '500',
                                                        'id': 'user-input',
                                                        'style': 'width:535px;'
                                                                 'height:70px; resize:none'}))

    class Meta:
        model = Message
        fields = ('text', )
