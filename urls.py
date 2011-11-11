from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    (r'^register/$', 'register.views.index'),
	(r'^register/success/$', 'register.views.process'),

)
