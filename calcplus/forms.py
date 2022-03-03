from django import forms

class CalcPlusForm(forms.Form):
    val1 = forms.IntegerField()
    val2 = forms.IntegerField()

#https://docs.djangoproject.com/en/4.0/ref/forms/fields/
