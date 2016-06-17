from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout

from imageManager.models import Image, Gallery, GalleryImage
# Create your views here.

class initialDatabaseSetup(View):
    def get(self, request):
        from datetime import datetime    

        arena1 = Image(image = "arena1.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena1.save()
        arena2 = Image(image = "arena2.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena2.save()
        arena3 = Image(image = "arena3.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena3.save()
        arena4 = Image(image = "arena3.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena4.save()
        arena5 = Image(image = "arena3.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena5.save()
        
        gallery1 = Gallery(gallery = "Indoor Riding Arena", galleryDescription="Indoor riding arena 60x160", create_dt = datetime.now(), edit_dt = datetime.now())
        gallery1.save()
        
        GalleryImage(isCover=True,galleryID_fk=gallery1,imageID_fk=arena1).save()
        GalleryImage(isCover=True,galleryID_fk=gallery1,imageID_fk=arena2).save()
        GalleryImage(isCover=True,galleryID_fk=gallery1,imageID_fk=arena3).save()
        GalleryImage(isCover=True,galleryID_fk=gallery1,imageID_fk=arena4).save()
        GalleryImage(isCover=True,galleryID_fk=gallery1,imageID_fk=arena5).save()
        
        context = {"pageName": "initializeData", "pageTitle": "Database Setup"}
        
        return render_to_response("homePage.html",context_instance=RequestContext(request, context))