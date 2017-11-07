__author__ = 'pridemai'
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect

from models import *
# from functions import authenticate
from auth_functions import do_auth, do_logout
import json
# Python logging package
import logging

# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)

class SimpleClass:
    def __init__(self):

        self.var1 = "some var"
        self.var2='another var'

    def to_string(self):
        return str(self)

    def test(self, t):
        print t
    def __str__(self):
        return self.var1+" "+self.var2
def index(request):
    # print "something happened1"
    # stdlogger.info("Call to contactform method")
    # stdlogger.error("something happened")

    return render(request, 'index.html', {'test': "my data","simple_class":SimpleClass(), "variables":["1","2","3"]})

def login(request):
    return do_auth(request)


def logout(request):
    do_logout(request)
    return HttpResponseRedirect("/")
    # return do_logout(request)


# def do_login(request):
#
#     authenticate(request)
#
#     return HttpResponse(reversed("index"))
#

def candidates_all(request):
    candidates = []
    for c in Candidate.objects.all():
        candidates.append({"first_name": c.first_name, "last_name": c.last_name, "career_opportunity_name": c.career_opportunity.source_name,
                           "career_opportunity_url": c.career_opportunity.source_url, "career_opportunity_content": c.career_opportunity.content,
                           "background_name": c.background.background_name, "background_content":c.background.background_content})

    return HttpResponse(json.dumps(candidates))
def candidate_get(request, candidate_id=1):
    c = Candidate.objects.get(id=candidate_id)
    return HttpResponse(json.dumps({"first_name": c.first_name, "last_name": c.last_name,
                                    "career_opportunity_name": c.career_opportunity.source_name,
                                    "career_opportunity_url": c.career_opportunity.source_url,
                                    "career_opportunity_content": c.career_opportunity.content,
                                    "background_name": c.background.background_name,
                                    "background_content": c.background.background_content}
    ))
def background_get(request, candidate_id=1):
    c = Candidate.objects.get(id=candidate_id)
    return HttpResponse(json.dumps({"background_name": c.background.background_name,"background_content": c.background.background_content}))
def career_opportunity_get(request, candidate_id=1):
    c = Candidate.objects.get(id=candidate_id)
    return HttpResponse(json.dumps({"career_opportunity_name": c.career_opportunity.source_name,"career_opportunity_url": c.career_opportunity.source_url,"career_opportunity_content": c.career_opportunity.content,}))

def candidate_get_name(request, name_contains):
    candidates = []
    for c in Candidate.objects.all():
        candidates.append({"first_name": c.first_name, "last_name": c.last_name,
                           "career_opportunity_name": c.career_opportunity.source_name,
                           "career_opportunity_url": c.career_opportunity.source_url,
                           "career_opportunity_content": c.career_opportunity.content,
                           "background_name": c.background.background_name,
                           "background_content": c.background.background_content})

    return HttpResponse(json.dumps(candidates))