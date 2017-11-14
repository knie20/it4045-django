from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'it4045app.views.index', name='index'),
    url(r'^login/', 'it4045app.views.login', name="authenticate"),
    url(r'^logout/', 'it4045app.views.logout', name="logout"),
    url(r'^foo/', 'it4045app.views.foo', name="foo"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
