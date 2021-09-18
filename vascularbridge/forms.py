from django import forms
from .models import vascularBridgeRegister, limbIndexSym, limbIndexRutherford, limbIndexDiagnosis, limbPlansurgical
from .options import *

class PostRegister(forms.ModelForm):
    leftLimbIndex = forms.ModelMultipleChoiceField(queryset=limbIndexSym.objects.all(),widget=forms.CheckboxSelectMultiple)
    leftLimbRutherford = forms.ModelMultipleChoiceField(queryset=limbIndexRutherford.objects.all(), widget=forms.CheckboxSelectMultiple)
    leftLimbDiagnosis = forms.ModelMultipleChoiceField(queryset=limbIndexDiagnosis.objects.all(), widget=forms.CheckboxSelectMultiple)
    rightLimbIndex = forms.ModelMultipleChoiceField(queryset=limbIndexSym.objects.all(),widget=forms.CheckboxSelectMultiple)
    rightLimbRutherford = forms.ModelMultipleChoiceField(queryset=limbIndexRutherford.objects.all(), widget=forms.CheckboxSelectMultiple)
    rightLimbDiagnosis = forms.ModelMultipleChoiceField(queryset=limbIndexDiagnosis.objects.all(), widget=forms.CheckboxSelectMultiple)

    planSurgical = forms.ModelMultipleChoiceField(queryset=limbPlansurgical.objects.all())
     
    class Meta:
        model = vascularBridgeRegister
        fields = '__all__'
