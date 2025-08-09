from django.db import models
#from django.contrib.auth.models import User

class ChatConversation(models.Model):
    sender = models.CharField(max_length=10)  # "user" or "bot"
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
