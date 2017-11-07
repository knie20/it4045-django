# __author__ = 'pridemai'
#
# from django.db import models
#
# class CareerOpportunity(models.Model):
#     source_name=models.CharField(max_length=50)
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
