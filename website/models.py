from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User

class Sms(models.Model):
    name            = models.CharField(max_length=150, null=True, blank=True)
    email         = models.EmailField(null=True, blank=True)
    message      = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subscriberlist(models.Model):
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    abstract = models.TextField(null=True, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(default = 'post_photo.jpg', upload_to="post_pics", null=True, blank=True)
    

    def __str__(self):
        return self.title

