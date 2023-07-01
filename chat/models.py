from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self', blank=True)
    pfp = models.ImageField(upload_to='pfps/', null=True)
    about = models.TextField(max_length=130, null=True)
    status = models.CharField(max_length=100)
    online = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)
    
class Chat(models.Model):
    members = models.ManyToManyField(Profile)

    def __str__(self):
        return str(self.members)
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE, null=True)
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.text)


