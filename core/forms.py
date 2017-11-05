from django import forms

class BmiForm(forms.Form):
    """
    height is in meters
    weight is in kg
    """
    name = forms.CharField(required=False)
    height = forms.FloatField(label="Height in meters:", required=True, min_value=0)
    weight = forms.FloatField(label="Weight in kg:", required=True, min_value=0)
