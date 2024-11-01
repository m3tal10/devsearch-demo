from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class ChatMessage(models.Model):
    room_name= models.CharField(max_length=2000)
    sender= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    recipient= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    message= models.CharField(max_length=2000)
    created_at= models.DateTimeField(auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=['room_name']),
        ]
