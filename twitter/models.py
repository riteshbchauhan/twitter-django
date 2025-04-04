from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Twitter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length = 240)
    image = models.ImageField(upload_to = "photos/", blank=True, null = None)
    
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user.username} - {self.text}'
    