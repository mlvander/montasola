from models import Images

class Gallary:
    gallary = []
    
    def __init__ (self,gallaryID):
        images = Images.objects.all()
        
        for thisImage in images:
            image['file'] = image.image
            image['caption'] = image.imageDescription
            
            self.gallary.append(image)
    
    def getGallary(self):
        return self.gallary