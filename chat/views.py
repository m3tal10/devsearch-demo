from django.shortcuts import render
from .forms import SendMessageForm
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import ChatMessage
# Create your views here.
@login_required(login_url='login')
def chat_room(request,user_id):
    form= SendMessageForm()
    recipient= Profile.objects.get(id=user_id)
    sender_name= request.user.profile.username
    room_name= f"{recipient.username}_{sender_name}"

    context={
        'recipient':recipient,
        'form':form,
        'room_name':room_name,
        'sender':request.user.id,
        }
    return render(request,'chats/message.html',context)