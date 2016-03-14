from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=15)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Article(models.Model):
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article)
    
    def __str__(self):
        return self.content   