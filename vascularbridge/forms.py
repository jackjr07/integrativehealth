from django import forms
from .models import vascularBridgeRegister, limbIndexSym, limbIndexRutherford, limbIndexDiagnosis, limbSurgicalPlan, limbNonSurgicalPlan
from .options import *
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'

class PostRegister(forms.ModelForm):
    leftLimbIndex = forms.ModelMultipleChoiceField(queryset=limbIndexSym.objects.all(),widget=forms.CheckboxSelectMultiple)
    leftLimbRutherford = forms.ModelMultipleChoiceField(queryset=limbIndexRutherford.objects.all(), widget=forms.CheckboxSelectMultiple)
    leftLimbDiagnosis = forms.ModelMultipleChoiceField(queryset=limbIndexDiagnosis.objects.all(), widget=forms.CheckboxSelectMultiple)
    rightLimbIndex = forms.ModelMultipleChoiceField(queryset=limbIndexSym.objects.all(),widget=forms.CheckboxSelectMultiple)
    rightLimbRutherford = forms.ModelMultipleChoiceField(queryset=limbIndexRutherford.objects.all(), widget=forms.CheckboxSelectMultiple)
    rightLimbDiagnosis = forms.ModelMultipleChoiceField(queryset=limbIndexDiagnosis.objects.all(), widget=forms.CheckboxSelectMultiple)
    planSurgical = forms.ModelMultipleChoiceField(queryset=limbSurgicalPlan.objects.all())
    planNonSurgical = forms.ModelMultipleChoiceField(queryset=limbNonSurgicalPlan.objects.all())
     
    class Meta:
        model = vascularBridgeRegister
        fields = '__all__'
        widgets = {
            'OrPlanDate' : forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
            'preOpAppt':forms.NullBooleanSelect(),
            'preOpApptdate' : forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
        }
