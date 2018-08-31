from django import forms
from . import models

class CreateTwit(forms.ModelForm):
    class Meta:
        model = models.Twit
        fields = ['body']
        
       
        