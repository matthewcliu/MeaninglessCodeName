from django import forms
from meaninglesscodename.core import data_request

class DataRequestForm(forms.Form):
    latitude = forms.IntegerField()
    longitude = forms.IntegerField()
    distance_range = forms.IntegerField(required = False)
    time = forms.DateTimeField()
    time_range = forms.IntegerField(required = False)
    categories = forms.CharField(max_length=256, required = False)
    entities = forms.CharField(max_length=256, required = False)
    
    def form_to_obj_storage(form):
        data_request_obj = data_request.DataRequest()
            
        data_request_obj.latitude = form.cleaned_data['latitude']
        data_request_obj.longitude = form.cleaned_data['longitude']
        data_request_obj.distance_range = form.cleaned_data['distance_range']
        data_request_obj.time = form.cleaned_data['time']
        data_request_obj.time_range = form.cleaned_data['time_range']
        #Temporary solution for splitting categories - FRAGILE CODE
        if form.cleaned_data['categories'] is not None:
            data_request_obj.categories = form.cleaned_data['categories'].split()
        #Temporary solution for storing entity as a list - FRAGILE CODE
        if form.cleaned_data['entities'] is not None:
            data_request_obj.entities = form.cleaned_data['entities'].split()
            
        return data_request_obj