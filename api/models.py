from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Donator(models.Model):
    pass

class Receiver(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    rgct = models.BigIntegerField(blank=False, default=0)
    position = models.IntegerField(blank=False, default=0)
    abo = models.CharField(max_length=3, blank=False, default='')
    age = models.IntegerField(blank=False, default=0)
    panel = models.IntegerField(blank=False, default=0)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Acceptance(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
