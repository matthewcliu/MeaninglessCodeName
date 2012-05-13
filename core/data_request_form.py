from django import forms
from meaninglesscodename.core import data_request

class DataRequestForm(forms.Form):
    latitude = forms.IntegerField()
    longitude = forms.IntegerField()
    distance_range = forms.IntegerField(required = False)
    time = forms.DateTimeField()
    time_range = forms.IntegerField(required = False)
    categories_list = forms.CharField(max_length=256, required = False)
    entities_list = forms.CharField(max_length=256, required = False)
    
    def form_to_obj_storage(form):
        data_request_obj = data_request.DataRequest()
            
        data_request_obj.latitude = form.cleaned_data['latitude']
        data_request_obj.longitude = form.cleaned_data['longitude']
        data_request_obj.distance_range = form.cleaned_data['distance_range']
        data_request_obj.time = form.cleaned_data['time']
        data_request_obj.time_range = form.cleaned_data['time_range']
        #Temporary solution for splitting categories - FRAGILE CODE
        if form.cleaned_data['categories_list'] is not None:
            data_request_obj.categories_list = form.cleaned_data['categories_list'].split()
        #Temporary solution for storing entity as a list - FRAGILE CODE
        if form.cleaned_data['entities_list'] is not None:
            data_request_obj.entities_list = form.cleaned_data['entities_list'].split()
            
        return data_request_obj