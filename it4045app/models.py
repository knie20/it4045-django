# __author__ = 'pridemai'
#
from django.db import models
class Transmission(models.Model):
    type = models.CharField(max_length=100)
    speed = models.IntegerField(default=3)

    def __str__(self):
        return "%s Speed %s" %(self.speed, self.type)
class Motor(models.Model):
    displacement = models.IntegerField(default=100)
    family = models.CharField(max_length=100)
    horsepower =models.IntegerField(default=10)
    rpm = models.IntegerField(default=1000)

    def __str__(self):
        return "%s %s" %(self.displacement, self.family)

class CarDescription(models.Model):
    description = models.CharField(max_length=250)
    motor = models.OneToOneField(Motor)
    transmission =  models.OneToOneField(Transmission)
    mileage = models.IntegerField(default=0)
    mpg = models.CharField(max_length=500)

    def __str__(self):
        return "%s %s" %(self.motor, self.transmission)
class Car(models.Model):
    make=models.CharField(max_length=50)
    model = models.CharField(max_length=70)
    year = models.IntegerField(default=0)
    color = models.CharField(max_length=25)
    description = models.OneToOneField(CarDescription)
    def __str__(self):
        return "%s %s %s %s" % (self.year, self.color,self.make, self.model )




# class CareerOpportunity(models.Model):
#     source_name=gmodels.CharField(max_length=50)
#     source_url = models.CharField(max_length=500)
#     content = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.source_name
#
# class Background(models.Model):
#     background_name = models.CharField(max_length=50)
#     background_content = models.CharField(max_length=2000)
#
#
#     def __str__(self):
#         return self.background_name
#
#
# class Candidate(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     career_opportunity = models.ForeignKey(CareerOpportunity)
#     background = models.ForeignKey(Background)
#
#     def __str__(self):
#         return "%s %s"%(self.first_name, self.last_name)
#
#
