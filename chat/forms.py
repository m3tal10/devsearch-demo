from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import ChatMessage

class SendMessageForm(ModelForm):
    class Meta:
        model=ChatMessage
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'chat-message', 'placeholder':'Type your message...'})