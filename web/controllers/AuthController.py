from meaninglesscodename.web.controllers.BaseController import BaseController
from meaninglesscodename.core.models import UserNode 
from meaninglesscodename import settings

#from meaninglesscodename.core.lib import facebook

from django.contrib.auth import login, logout

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
    filename = '/tmp/debug.log',
    filemode = 'w'
)

class AuthController(BaseController):

"""
    def render_login(self):
        
        fb_user = facebook.get_user_from_cookie(self.request.COOKIES,
                                                settings.FACEBOOK_APP_ID,
                                                settings.FACEBOOK_SECRET_KEY)

        next=self.request.GET.get('next')

        if not fb_user:
            raise Exception("HERE")
            return self.redirect(self.reverse('index'))

        at = fb_user.get('access_token', '')
        fuid = fb_user.get('uid', '')

        usernode, is_created = UserNode.objects.handle_user(fuid, at)

        if usernode is None:
            return self.redirect(self.reverse('index'))

        usernode.user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, usernode.user)

        return self.redirect(next)
        

    def render_logout(self):
        logout(self.request)
        return self.redirect(self.reverse('index'))
"""