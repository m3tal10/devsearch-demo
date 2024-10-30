from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatMessage(models.Model):
    room_name= models.CharField(max_length=2000)
    sender= models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.CharField(max_length=2000)
    created_at= models.DateTimeField(auto_now=True)