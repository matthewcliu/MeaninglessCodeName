from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

class BaseController(object):

    def __init__(self, request):
        self.request = request

    def render_to_response(self, template, template_data={}):
        return render_to_response(template, template_data, \
            context_instance=RequestContext(self.request))

    def redirect(self, url):
        return HttpResponseRedirect(url)

    def reverse(self, name, args=None):
        return reverse(name, args=args)

    def render(self, message):
        return HttpResponse(message)
