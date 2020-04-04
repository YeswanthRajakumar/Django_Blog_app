from django.db import models
from django.utils import timezone

'''
For one-to- many relationship
--  One Author may have many posts
--  Many Posts may have one  Author'''

from django.contrib.auth.models import User


# Create your models her e.

class Post(models.Model):
    title = models.CharField(max_length=50)
    post_content = models.TextField(max_length=600)
    posted_time = models.DateTimeField(default=timezone.now())
    # if  author's account was deleted then delete his posts
    author = models.ForeignKey(User,on_delete=models.CASCADE)

# This method returns title while we work on Terminal

    def __str__(self):
        return self.title
