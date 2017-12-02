from django.db import models

class Tweet(models.Model):
    tweetId = models.BigIntegerField(default=0)
    userId = models.BigIntegerField(default=0)
    text = models.CharField(max_length=300)
    createdAt = models.DateTimeField()
    def __str__(self):
        return "%s %s %s %s" % (self.tweetId, self.userId, self.text, self.createdAt)

class TwitterUser(models.Model):
    userId = models.BigIntegerField(default=0)
    handle = models.CharField(max_length=15)
    displayName = models.CharField(max_length=20)