from django.http import HttpResponse
from django.shortcuts import render_to_response
from meaninglesscodename.core.models import *
from django.contrib.auth.decorators import login_required

import time

def index(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_index()

def login(request):
    from meaninglesscodename.web.controllers.AuthController import AuthController
    ac = AuthController(request)
    return ac.render_login()

def logout(request):
    from meaninglesscodename.web.controllers.AuthController import AuthController
    ac = AuthController(request)
    return ac.render_logout()

def skeleton(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_skeleton()

def base(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_base()

"""
@login_required(login_url='/')
def home(request):
    from wedding.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.handle_home()

@login_required(login_url='/')
def upload(request, event=None):
    from wedding.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.handle_upload(event)

@login_required(login_url='/')
def album(request, event=None):
    from wedding.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.handle_album(event)

@login_required(login_url='/')
def preview(request, event=None):
    from wedding.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.handle_preview(event)

def ajax_vote(request):
    from wedding.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.handle_ajax_vote()
"""

# Static Pages (please put at the bottom of this controller)
def about(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_about()

def howitworks(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_howitworks()

def faq(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_faq()

def terms(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_terms()

def contact(request):
    from meaninglesscodename.web.controllers.IndexController import IndexController
    ic = IndexController(request)
    return ic.render_contact()
