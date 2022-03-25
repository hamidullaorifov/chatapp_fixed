from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Chat(models.Model):
    user1 = models.ForeignKey(User,related_name='chats1',on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,related_name='chats2',on_delete=models.CASCADE)
    
class Message(models.Model):
    
    messageText = models.TextField()
    # messageFile = models.FileField(upload_to='files/',null=True,blank=True,)
    # messageImage = models.ImageField(upload_to='images/',null=True,blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_messages')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='received_messages')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)




