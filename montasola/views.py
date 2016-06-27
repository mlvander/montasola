from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout

class homePage(View):
    def get(self, request):
        pageTitleTag = "Home"  
        pageHeading  = "Welcome to Montasola Farms"      
        
        context = {"pageTitleTag": pageTitleTag, "pageHeading": pageHeading}

        return render_to_response("homePage.html",context_instance=RequestContext(request, context))
    
class about(View):
    def get(self, request):
        pageTitleTag = "About"
        pageHeading = "About Montasola Farms"
        
        context = {"pageTitleTag": pageTitleTag, "pageHeading": pageHeading}

        return render_to_response("about.html",context_instance=RequestContext(request, context))
    
class schedule(View):
    def get(self, request):
        pageTitleTag  = "Schedule"
        pageHeading = "Montasola Farms Schedule"
        
        context = {"pageTitleTag": pageTitleTag, "pageHeading": pageHeading}

        return render_to_response("schedule.html",context_instance=RequestContext(request, context))
    
class contact(View):
    def get(self, request):
        pageTitleTag  = "Contact"
        pageHeading = "Contact Us"
        
        context = {"pageTitleTag": pageTitleTag, "pageHeading": pageHeading}

        return render_to_response("contact.html",context_instance=RequestContext(request, context))