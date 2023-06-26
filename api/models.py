from django.db import models

class Donator(models.Model):
    pass

class Receiver(models.Model):
    pass

class User(models.Model):
    pass

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
