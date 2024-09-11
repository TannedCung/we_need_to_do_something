from django import forms
from .models import Victim, Rescuer, Guest

class VictimForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = ['name', 'phone', 'location_lat', 'location_lon', 'need']

class RescuerForm(forms.ModelForm):
    class Meta:
        model = Rescuer
        fields = ['name', 'phone', 'location_lat', 'location_lon', 'specialization']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'phone', 'message']
