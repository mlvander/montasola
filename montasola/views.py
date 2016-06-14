from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout

class homePage(View):
    def get(self, request):
        pageTile = "Welcome to Montasola Farms Events"
        pageName = "Events"        
        
        context = {"pageName": pageName, "pageTitle": pageTile}

        return render_to_response("homePage.html",context_instance=RequestContext(request, context))