# forms.py


# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate

class CandidateRegistrationForm(UserCreationForm):
    respiration_rate = forms.FloatField()
    body_temperature=forms.FloatField()
    blood_oxygen_levels=forms.FloatField()
    eye_movement=forms.FloatField()
    hours_of_sleep=forms.FloatField()



    class Meta(UserCreationForm.Meta):
        model = Candidate
        fields = UserCreationForm.Meta.fields + ('respiration_rate','body_temperature','blood_oxygen_levels','eye_movement','hours_of_sleep') # Include other fields as needed
        exclude = ('username',) 
        
        
        
        # stressapp/forms.py
from django import forms

class StressPredictionForm(forms.Form):
    respiration_rate = forms.FloatField(label='Respiration Rate')
    body_temperature = forms.FloatField(label='Body Temperature')
    blood_oxygen_levels = forms.FloatField(label='Blood Oxygen Levels')
    eye_movement = forms.FloatField(label='Eye Movement')
    hours_of_sleep = forms.FloatField(label='Number of Hours of Sleep')
