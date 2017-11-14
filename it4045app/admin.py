__author__ = 'pridemai'
from django.contrib import admin
from models import Car, CarDescription, Motor, Transmission
admin.site.register(Car)
admin.site.register(CarDescription)
admin.site.register(Motor)
admin.site.register(Transmission)
# admin.site.register(Candidate)
# admin.site.register(Background)
