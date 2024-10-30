from django.urls import path
from . import views

urlpatterns=[
    # path('<str:room_name>/',views.chat_room),
    path('chat-message/<str:user_id>/',views.chat_room)
]