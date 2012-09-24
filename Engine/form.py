from django.db import models
from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
class FirstInvitationForm(forms.Form):
    Email = forms.EmailField(max_length=100)
    forms.CharField(label='Demande',widget=forms.Textarea)
    CARAC_CHOICES = (('1', 'Nul'), ('2', 'Bof'),('3', 'Moyen'),('4', 'Bon'),('5', 'Excellent'))
    PRIVATE_CHOICES = (('0', 'Private'), ('1', 'Public'))
    carac_level = ChoiceField(label='Niveau : ',widget=RadioSelect, choices=CARAC_CHOICES,initial=1)