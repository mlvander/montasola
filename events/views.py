from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout

class events(View):
    def get(self, request):
        pageTitleTag = "Events"  
        pageHeading  = "Montasola Farms Events"      
        
        context = {"pageTitleTag": pageTitleTag, "pageHeading": pageHeading}

        return render_to_response("events.html",context_instance=RequestContext(request, context))
    