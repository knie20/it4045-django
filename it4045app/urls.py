from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'it4045app.views.index', name='index'),
    url(r'^login/', 'it4045app.views.login', name="authenticate"),
    url(r'^logout/', 'it4045app.views.logout', name="logout"),
    # url(r'^do_login/', 'it4045app.views.do_login', name="authenticate"),
    # url(r'^candidates/all/', 'it4045app.views.candidates_all', name="candidates_all"),
    # url(r'^candidate/(?P<candidate_id>\d+)/', 'it4045app.views.candidate_get', name="candidate_get"),
    # url(r'^candidate/(?P<name_contains>\s+)/', 'it4045app.views.candidate_get_name', name="candidate_get_name"),
    # url(r'^background/(?P<candidate_id>\d+)/', 'it4045app.views.background_get', name="background_get"),
    # url(r'^career_opportunity/(?P<candidate_id>\d+)/', 'it4045app.views.career_opportunity_get', name="career_opportunity"),
    #
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
