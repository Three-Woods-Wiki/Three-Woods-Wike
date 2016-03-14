from django.contrib import admin

# Register your models here.
from wiki.models import UserProfile, Article, Comment

admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Comment)