from models import Images

class Gallery:
    gallery = []
    
    def __init__ (self,galleryID):
        images = Images.objects.all()
        
        for thisImage in images:
            image['file'] = image.image
            image['caption'] = image.imageDescription
            
            self.gallery.append(image)
    
    def getGallary(self):
        return self.gallery