from django import forms
from .models import Donator, Patient, Receiver

class DonatorForm(forms.ModelForm):
    class Meta:
        model = Donator
        fields = ('report',
                    'name',
                    'rgct',
                    'date',
                    'location',
                    'opo',
                    'height',
                    'age',
                    'gender',
                    'death_cause',
                    'cr_in',
                    'cr_out',
                    'hypertension',
                    'diabetes',
                    'hbsag',
                    'anti_hcv',
                    'avch_death',
                    'chagas',
                    'anti_hbs',
                    'hltv',
                    'vdrl',
                    'anti_hbc',
                    'hiv',
                    'toxoplasmosis',
                    'age_50_60',
                    'cr_in_greater_than_15')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'rgct', 'position', 'abo', 'age', 'panel')
    
class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ('name', 'rgct', 'position', 'abo', 'age', 'panel')