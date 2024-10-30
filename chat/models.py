from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    room_id= models.CharField(max_length=255,unique=True)
class ChatMessage(models.Model):
    # room_id=models.ForeignKey(Room,on_delete= models.CASCADE)
    # sender= models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.CharField(max_length=2000)
    created_at= models.DateTimeField(auto_now=True)