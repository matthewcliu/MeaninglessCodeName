from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from meaninglesscodename.web.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('meaninglesscodename.web.views',
    # Examples:
    # url(r'^$', 'wedding.views.home', name='home'),
    # url(r'^wedding/', include('bookmarklet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url('^$', 'index', name='index'),
    url('^login$', 'login', name='login'),
    url('^logout$', 'logout', name='logout'),
    url('^home$', 'home', name='home'),
    url('^listing$', 'listing', name='listing'),
    url('^testmap$', 'testmap', name='testmap'),

	# These are the static pages (please put these at the bottom)
    url('^skeleton$', 'skeleton', name='skeleton'),
    url('^base$', 'base', name='base'),
    url('^about$', 'about', name='about'),
    url('^howitworks$', 'howitworks', name='howitworks'),
    url('^faq$', 'faq', name='faq'),
    url('^terms$', 'terms', name='terms'),
    url('^contact$', 'contact', name='contact'),

)

# Adds all the static files
urlpatterns += staticfiles_urlpatterns()
