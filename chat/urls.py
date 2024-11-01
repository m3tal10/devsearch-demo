from django.urls import path
from . import views

urlpatterns=[
    path('inbox/',views.inbox, name='chat-inbox'),
    path('chat-message/<str:user_id>/',views.chat_room, name='chat-message')
]