from django import forms
from .models import Message,Direct_Service

class MyMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['full_name','email','subject','message']



class Direct_Message_sevice(forms.ModelForm):
    class Meta:
        model = Direct_Service
        fields = ['full_name','email','service_type','phone_number']