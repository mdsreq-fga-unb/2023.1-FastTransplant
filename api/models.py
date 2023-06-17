from django.db import models
import string
import random

def generate_unique_code():
    length = 9

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Rim.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Rim(models.Model):
    code = models.CharField(max_length=9, default="", unique=True)
    medico = models.CharField(max_length=20, default='padrão', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)