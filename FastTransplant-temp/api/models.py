from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    crm = models.CharField(max_length=9, blank=False)

class Organ(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=100, blank=False)
    rgct = models.IntegerField(blank=False)
    date = models.DateField(blank=False)
    location  = models.CharField(max_length=100, blank=False)
    opo = models.CharField(max_length=100, blank=False)
    height = models.DecimalField(blank=False)
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
    age = models.IntegerField(blank=False)
    transplant_date = models.DateField(blank=False)