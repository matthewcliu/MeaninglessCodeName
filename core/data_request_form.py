from django import forms

class DataRequestForm(forms.Form):
    latitude = forms.IntegerField()
    longitude = forms.IntegerField()
    distance_range = forms.IntegerField(required = False)
    time = forms.DateTimeField()
    time_range = forms.IntegerField(required = False)
    categories = forms.CharField(max_length=256, required = False)
    entities = forms.CharField(max_length=256, required = False)