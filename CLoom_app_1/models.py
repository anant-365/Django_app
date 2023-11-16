from django.db import models


# Create your models here.
class Features(models.Model):
    header = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    button_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class UserDetails(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=30, default='Not set')
    bio = models.CharField(max_length=110, default='Not set')
    profile_pic = models.ImageField(default='https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg')

    def __str__(self):
        return self.username
