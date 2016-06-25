from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout

from imageManager.models import Image, Gallery, GalleryImage

from django.db import connection

class imageGalleries(View):
    def get(self, request):
        
        galleries = GalleryImage.objects.filter(isCover=True)
        
        context = {"pageName": "Image Galleries", "pageTitle": "Galleries", "galleries": galleries}
        
        return render_to_response("galleries.html",context_instance=RequestContext(request, context))

class imageGallery(View):
    def get(self, request, galleryID):
        
        gallery = GalleryImage.objects.filter(galleryID_fk=Gallery.objects.get(pk=galleryID))
        
        context = {"pageName": "Image Galleries", "pageTitle": "Galleries", "gallery": gallery}
        
        return render_to_response("gallery.html",context_instance=RequestContext(request, context))





class initialDatabaseSetup(View):
    def get(self, request):
        from datetime import datetime    

        #need to use a direct Mysql cursor to access the dataset for this questionnaire
        cursor = connection.cursor()
        cursor.execute("DELETE FROM imageManager_galleryimage WHERE galleryimageID >0;")
        cursor.execute("ALTER TABLE imageManager_galleryimage AUTO_INCREMENT = 1;")
        connection.commit()
        
        cursor = connection.cursor()
        cursor.execute("DELETE FROM imageManager_image WHERE imageID >0;")
        cursor.execute("ALTER TABLE imageManager_image AUTO_INCREMENT = 1;")
        connection.commit()
        
        cursor = connection.cursor()
        cursor.execute("DELETE FROM imageManager_gallery WHERE galleryID >0;")
        cursor.execute("ALTER TABLE imageManager_gallery AUTO_INCREMENT = 1;")
        connection.commit()
            
        arena1 = Image(image = "arena1.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena1.save()
        arena2 = Image(image = "arena2.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena2.save()
        arena3 = Image(image = "arena3.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena3.save()
        arena4 = Image(image = "arena4.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena4.save()
        arena5 = Image(image = "arena5.jpg", imageDescription = "Our Indoor Riding Space", create_dt = datetime.now(), edit_dt = datetime.now())
        arena5.save()
        
        gallery1 = Gallery(gallery = "Indoor Riding Arena", galleryDescription="Indoor riding arena 60x160", create_dt = datetime.now(), edit_dt = datetime.now())
        gallery1.save()
        
        GalleryImage(isCover=True,galleryID_fk=gallery1,imageID_fk=arena1).save()
        GalleryImage(isCover=False,galleryID_fk=gallery1,imageID_fk=arena2).save()
        GalleryImage(isCover=False,galleryID_fk=gallery1,imageID_fk=arena3).save()
        GalleryImage(isCover=False,galleryID_fk=gallery1,imageID_fk=arena4).save()
        GalleryImage(isCover=False,galleryID_fk=gallery1,imageID_fk=arena5).save()
        
        farm1 = Image(image = "farm1.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm1.save()
        farm2 = Image(image = "farm2.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm2.save()
        farm3 = Image(image = "farm3.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm3.save()
        farm4 = Image(image = "farm4.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm4.save()
        farm5 = Image(image = "farm5.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm5.save()
        farm6 = Image(image = "farm6.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm6.save()
        farm7 = Image(image = "farm7.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm7.save()
        farm8 = Image(image = "farm8.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm8.save()
        farm9 = Image(image = "farm9.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm9.save()
        farm10 = Image(image = "farm10.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm10.save()
        farm11 = Image(image = "farm11.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm11.save()
        farm12 = Image(image = "farm12.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm12.save()
        farm13 = Image(image = "misc1.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm13.save()
        farm14 = Image(image = "misc2.jpg", imageDescription = "The Farm", create_dt = datetime.now(), edit_dt = datetime.now())
        farm14.save()
        
        gallery2 = Gallery(gallery = "Our Farm", galleryDescription="We proudly maintain our facilities.", create_dt = datetime.now(), edit_dt = datetime.now())
        gallery2.save()
        
        GalleryImage(isCover=True,galleryID_fk=gallery2,imageID_fk=farm1).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm2).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm3).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm4).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm5).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm6).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm7).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm8).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm9).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm10).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm11).save()
        GalleryImage(isCover=False,galleryID_fk=gallery2,imageID_fk=farm12).save()
        
        jump1 = Image(image = "jumpbuild1.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump1.save()
        jump2 = Image(image = "jumpbuild2.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump2.save()
        jump3 = Image(image = "jumpbuild3.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump3.save()
        jump4 = Image(image = "jumpbuild4.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump4.save()
        jump5 = Image(image = "jumpbuild5.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump5.save()
        jump6 = Image(image = "jumper1.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump6.save()
        jump7 = Image(image = "jumper2.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump7.save()
        jump8 = Image(image = "jumper3.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump8.save()
        jump9 = Image(image = "jumper4.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump9.save()
        jump10 = Image(image = "jumper5.jpg", imageDescription = "Jumps", create_dt = datetime.now(), edit_dt = datetime.now())
        jump10.save()
        
        gallery3 = Gallery(gallery = "Montasola Jumper School", galleryDescription="Learn how to jump", create_dt = datetime.now(), edit_dt = datetime.now())
        gallery3.save()
        
        GalleryImage(isCover=True,galleryID_fk=gallery3,imageID_fk=jump1).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump2).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump3).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump4).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump5).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump6).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump7).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump8).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump9).save()
        GalleryImage(isCover=False,galleryID_fk=gallery3,imageID_fk=jump10).save()
        
        serve1 = Image(image = "sign1.jpg", imageDescription = "Facilities & Services", create_dt = datetime.now(), edit_dt = datetime.now())
        serve1.save()
        serve2 = Image(image = "stalls1.jpg", imageDescription = "Facilities & Services", create_dt = datetime.now(), edit_dt = datetime.now())
        serve2.save()
        serve3 = Image(image = "stalls2.jpg", imageDescription = "Facilities & Services", create_dt = datetime.now(), edit_dt = datetime.now())
        serve3.save()
        serve4 = Image(image = "stalls3.jpg", imageDescription = "Facilities & Services", create_dt = datetime.now(), edit_dt = datetime.now())
        serve4.save()
        serve5 = Image(image = "truck1.jpg", imageDescription = "Facilities & Services", create_dt = datetime.now(), edit_dt = datetime.now())
        serve5.save()
        serve6 = Image(image = "truck2.jpg", imageDescription = "Facilities & Services", create_dt = datetime.now(), edit_dt = datetime.now())
        serve6.save()
        
        gallery4 = Gallery(gallery = "Services", galleryDescription="Find out what we have to offer", create_dt = datetime.now(), edit_dt = datetime.now())
        gallery4.save()
        
        GalleryImage(isCover=True,galleryID_fk=gallery4,imageID_fk=serve1).save()
        GalleryImage(isCover=False,galleryID_fk=gallery4,imageID_fk=serve2).save()
        GalleryImage(isCover=False,galleryID_fk=gallery4,imageID_fk=serve3).save()
        GalleryImage(isCover=False,galleryID_fk=gallery4,imageID_fk=serve4).save()
        GalleryImage(isCover=False,galleryID_fk=gallery4,imageID_fk=serve5).save()
        GalleryImage(isCover=False,galleryID_fk=gallery4,imageID_fk=serve6).save()
        
        context = {"pageName": "initializeData", "pageTitle": "Database Setup"}
        
        return render_to_response("homePage.html",context_instance=RequestContext(request, context))