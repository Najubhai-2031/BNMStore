from email.policy import default
from enum import unique
from django.db import models



class news(models.Model):
    news_title=models.CharField(max_length=100)
    news_desc=models.TextField()
    news_image=models.FileField(upload_to="news/", max_length=250, null=True, default=None)

# Create your models here.
