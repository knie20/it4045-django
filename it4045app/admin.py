__author__ = 'pridemai'
from django.contrib import admin
from models import Tweet, TwitterUser

admin.site.register(Tweet)
admin.site.register(TwitterUser)

