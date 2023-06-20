from django import forms
from .models import Donator, Patient, Receiver, OrganReport

class DonatorForm(forms.ModelForm):
    class Meta:
        model = Donator
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'rgct', 'position', 'abo', 'age', 'panel')
    
class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ('name', 'rgct', 'position', 'abo', 'age', 'panel')

class OrganReportForm(forms.Form):
    class Meta:
        model = OrganReport
        fields = ('file')