from django import forms
from .models import Organ, Pacient, User

class OrganForm(forms.ModelForm):
    class Meta:
        model = Organ
        fields = '__all__'

class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'