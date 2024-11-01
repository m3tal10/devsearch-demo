import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatMessage
from users.models import User,Profile
from datetime import timedelta

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name= f"chat_{self.room_name}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['content']
        sender= await sync_to_async(Profile.objects.get)(id= text_data_json['sender'])
        recipient= await sync_to_async(Profile.objects.get)(id= text_data_json['recipient'])
        new_message = await sync_to_async(ChatMessage.objects.create)(
            message= message,
            sender= sender,
            room_name= text_data_json['room_name'],
            recipient= recipient,
        )
        new_created_at= new_message.created_at+ timedelta(hours=6)
        formatted_created_at = new_created_at.strftime('%b. %d, %Y, %I:%M %p')
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'created_at': formatted_created_at
            }
        )
    async def chat_message(self, event):
        message = event['message']
        sender= event['sender']
        created_at= event['created_at']
        await self.send(text_data=json.dumps({
            'message': message,
            'sender':sender,
            'created_at':created_at
        }))