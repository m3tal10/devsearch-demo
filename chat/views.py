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
    sender_name= request.user.username
    room_name= f"{recipient.username}_{sender_name}"
    sorted_room_name= '_'.join(sorted(room_name.split('_')))
    messages= ChatMessage.objects.filter(room_name=sorted_room_name)

    context={
        'recipient':recipient,
        'form':form,
        'room_name':room_name,
        'sender':request.user.id,
        'sender_profile':request.user.profile,
        'messages':messages,
        }
    return render(request,'chats/message.html',context)