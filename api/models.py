from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    job = models.CharField(max_length=100, blank=False, default='')
    education = models.CharField(max_length=100, blank=False, default='')
    location = models.CharField(max_length=100, blank=False, default='')
    category = models.IntegerField(blank=False, default=1)
    class Meta:
        db_table = 'auth_user'

class Donator(models.Model):
    #gender_choices = ('M', 'Masculino'), ('F', 'Feminino')
    abo_choices = ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')

    report = models.FileField(upload_to='reports/', blank=True, default='')
    gender = models.CharField(blank=False, max_length=10)
    rgct = models.CharField(blank=False, max_length=100)
    date = models.DateField(blank=False)
    location  = models.CharField(max_length=100, blank=False, default='')
    abo = models.CharField(max_length=2, choices=abo_choices, blank=False, default='A')
    height = models.FloatField(blank=False, default=0)
    age = models.IntegerField(blank=False, default=0)
    #gender = models.CharField(max_length=1, choices=gender_choices, blank=False, default='M')
    death_cause = models.TextField(blank=False, default='')

class Receiver(models.Model):
    abo_choices = ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')

    name = models.CharField(max_length=100, blank=False, default='')
    rgct = models.CharField(blank=False, max_length=100)
    position = models.IntegerField(blank=False, default=0)
    abo = models.CharField(max_length=2, choices=abo_choices, blank=False, default='A')
    age = models.IntegerField(blank=False, default=0)
    panel = models.IntegerField(blank=False, default=0)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Acceptance(models.Model):
    decision_choices = ('A', 'Aceito'), ('R', 'Rejeitado')
    # compatibility_choices = ('C', 'Compatível'), ('I', 'Incompatível')

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    compatibility = models.BooleanField(default=True)
    decision = models.CharField(max_length=1, choices=decision_choices, blank=False, default='A')
    description = models.CharField(max_length=100)

class PasswordChangeRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_allowed = models.BooleanField(default=True)