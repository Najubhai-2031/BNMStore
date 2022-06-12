from django.db import models
from email.policy import default
from django.db import models


class contactenquiry(models.Model):
    contact_name=models.CharField(max_length=50)
    contact_email=models.CharField(max_length=50)
    contact_phone=models.CharField(max_length=10)
    contact_messege=models.TextField()

# Create your models here.
