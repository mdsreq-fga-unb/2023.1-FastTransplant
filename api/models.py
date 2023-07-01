from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Donator(models.Model):
    gender_choices = ('M', 'Masculino'), ('F', 'Feminino')

    report = models.FileField(upload_to='reports/', blank=True, default='')
    rgct = models.BigIntegerField(blank=False, default=0)
    date = models.CharField(blank=False, default='', max_length=10)
    location  = models.CharField(max_length=100, blank=False, default='')
    opo = models.CharField(max_length=100, blank=False, default='')
    height = models.FloatField(blank=False, default=0)
    age = models.IntegerField(blank=False, default=0)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=False, default='M')
    death_cause = models.TextField(blank=False, default='')

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
