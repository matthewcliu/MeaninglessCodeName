from django.middleware.csrf import get_token
from meaninglesscodename.web.controllers.BaseController import *
from meaninglesscodename.core.models import *
from meaninglesscodename import settings
from django.template.defaultfilters import slugify
from django.template import Context, loader
from datetime import *
from django.core import serializers
import simplejson
import re

from meaninglesscodename import constants

import logging
import simplejson

import sys

from meaninglesscodename.core import data_request 
from meaninglesscodename.core import data_request_handler
from meaninglesscodename.core import data_request_form
from meaninglesscodename.core import json_friendly

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
                                
                data_request_obj = data_request_form.DataRequestForm.form_to_obj_storage(form)                                                
                data_response_obj = data_request_handler.handle_request(data_request_obj)
                entity_instances_to_template = data_response_obj.entity_map_display_data_list
                json_entity_instances = simplejson.dumps(json_friendly.flatten_objects(entity_instances_to_template))
                
                params = { 'json_entity_instances': json_entity_instances, 'entity_instances_to_template': entity_instances_to_template, 'form':form }
                            
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