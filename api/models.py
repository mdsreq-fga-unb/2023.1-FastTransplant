from django.db import models

class OrganReport(models.Model):
    date = models.DateField(blank=False)
    file = models.FileField(upload_to='reports/')

class Donator(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    report = models.ForeignKey(OrganReport, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    rgct = models.IntegerField(blank=False)
    date = models.DateField(blank=False)
    location  = models.CharField(max_length=100, blank=False)
    opo = models.CharField(max_length=100, blank=False)
    height = models.FloatField(blank=False)
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=1, choices=gender_choices)
    death_cause = models.TextField(blank=False)
    cr_in = models.CharField(max_length=100, blank=False)
    cr_out = models.CharField(max_length=100, blank=False)
    hypertension = models.BooleanField(blank=False)
    diabetes = models.BooleanField(blank=False)
    hbsag = models.BooleanField(blank=False)
    anti_hcv = models.BooleanField(blank=False)
    avch_death = models.BooleanField(blank=False)
    chagas = models.BooleanField(blank=False)
    anti_hbs = models.BooleanField(blank=False)
    hltv = models.BooleanField(blank=False)
    vdrl = models.BooleanField(blank=False)
    anti_hbc = models.BooleanField(blank=False)
    hiv = models.BooleanField(blank=False)
    toxoplasmosis = models.BooleanField(blank=False)
    age_50_60 = models.BooleanField(blank=False)
    cr_in_greater_than_15 = models.BooleanField(blank=False)

class Pacient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    rgct = models.BigIntegerField(blank=False)
    position = models.IntegerField(blank=False)
    abo = models.CharField(max_length=3 ,blank=False)
    age = models.IntegerField(blank=False)
    panel = models.IntegerField(blank=False)

class Receiver(models.Model):
    name = models.CharField(max_length=100, blank=False)
    rgct = models.BigIntegerField(blank=False)
    position = models.IntegerField(blank=False)
    abo = models.CharField(max_length=3, blank=False)
    age = models.IntegerField(blank=False)
    panel = models.IntegerField(blank=False)

# MVP2
class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    crm = models.CharField(max_length=9, blank=False)