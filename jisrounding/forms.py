from django import forms

class JisroundingForm(forms.Form):
    value = forms.DecimalField(label = 'Measured value')
    digit = forms.IntegerField(label = 'Digit')
