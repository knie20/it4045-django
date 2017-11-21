from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'it4045app.views.index', name='index'),
    url(r'^login/', 'it4045app.views.login', name="authenticate"),
    url(r'^logout/', 'it4045app.views.logout', name="logout"),
    url(r'^foo/', 'it4045app.views.foo', name="foo"),
    url(r'^car_creation/', 'it4045app.views.car_creation', name="car_creation"),
    url(r'^filter_cars/', 'it4045app.views.filter_cars_view', name="filter_cars"),
    url(r'^car_creation_submit/', 'it4045app.views.car_creation_submit', name="car_creation_submit"),
    url(r'^edit_car_submit/', 'it4045app.views.edit_car_submit', name="edit_car_submit"),
    url(r'^edit_car/', 'it4045app.views.edit_car', name="edit_car"),
    url(r'^remove_car/', 'it4045app.views.remove_car', name="remove_car"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
