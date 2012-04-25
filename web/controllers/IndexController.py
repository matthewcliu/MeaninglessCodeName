from django.middleware.csrf import get_token
from meaninglesscodename.web.controllers.BaseController import *
from meaninglesscodename.core.models import *
from meaninglesscodename import settings
from django.template.defaultfilters import slugify
from django.template import Context, loader
from datetime import *
import re

from meaninglesscodename import constants

import logging
import simplejson

import sys

from meaninglesscodename.core import data_request 
from meaninglesscodename.core import data_request_handler
from meaninglesscodename.core import data_request_form

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
    filename = '/tmp/debug.log',
    filemode = 'w'
)

class IndexController(BaseController):

    def render_index(self):
        
        return self.render_to_response('index.html', {} )
        
    def render_listing(self):

        if self.request.method == 'POST': 
            form = data_request_form.DataRequestForm(self.request.POST) 
            
            if form.is_valid():
                
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
                                                
                data_request_results = data_request_handler.handle_request(data_request_obj)
                
                params = { 'data_request_results': data_request_results, 'form':form }
                
                return self.render_to_response('listing.html', params) # Redirect after POST
        else:
            form = data_request_form.DataRequestForm() # An unbound form

        params = { 'form': form }

        return self.render_to_response('listing.html', params)

    def render_skeleton(self):
        return self.render_to_response('skeleton.html', {})

    def render_base(self):
        return self.render_to_response('base.html', {})

    def render_about(self):
        
        return self.render_to_response('static-about.html', {})

    def render_howitworks(self):
        return self.render_to_response('static-howitworks.html', {})

    def render_faq(self):
        return self.render_to_response('static-faq.html', {})

    def render_terms(self):
        return self.render_to_response('static-terms.html', {})

    def render_contact(self):
        return self.render_to_response('static-contact.html', {})
