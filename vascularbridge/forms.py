from django import forms
from .models import vascularBridgeRegister

class PostRegister(forms.ModelForm):
    class Meta:
        model = vascularBridgeRegister
        fields = '__all__'
