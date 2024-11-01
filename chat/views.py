from django.shortcuts import render
from .forms import SendMessageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import ChatMessage
from datetime import timedelta

# Create your views here.
@login_required(login_url='login')
def chat_room(request,user_id):
    form= SendMessageForm()
    recipient= Profile.objects.get(id=user_id)
    sender_name= request.user.username
    room_name= f"{recipient.username}_{sender_name}"
    sorted_room_name= '_'.join(sorted(room_name.split('_')))
    messages= ChatMessage.objects.filter(room_name=sorted_room_name)
    for message in messages:
        message.created_at= (message.created_at+timedelta(hours=6)).strftime('%b. %d, %Y, %I:%M %p')
    context={
        'recipient':recipient.id,
        'form':form,
        'room_name':room_name,
        'sender':request.user.profile.id,
        'sender_profile':request.user.profile,
        'texts':messages,
        }
    return render(request,'chats/message.html',context)

@login_required(login_url='login')
def inbox(request):
    self_initiated_rooms = ChatMessage.objects.filter(sender=request.user.profile).values('room_name').distinct()
    others_initiated_rooms= ChatMessage.objects.filter(recipient=request.user.profile).values('room_name').distinct()
    unique_rooms= set([])
    conversations=[]
    for room in self_initiated_rooms:
        unique_rooms.add(room['room_name'])
    for room in others_initiated_rooms:
        unique_rooms.add(room['room_name'])
    for room in unique_rooms:
        conversation= ChatMessage.objects.filter(room_name=room).order_by('created_at').last()
        conversations.append(conversation)
    
    context={
        'conversations':conversations,
        'owner': request.user.profile.id,
        }
    return render(request, 'chats/inbox.html',context)