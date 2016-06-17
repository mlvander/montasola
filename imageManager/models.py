from django.db import models

# Create your models here.

class Image(models.Model):
    imageID = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)
    imageDescription = models.CharField(max_length=255)
    create_dt = models.DateField()
    edit_dt = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.imageID)

    def __str__(self):
        return u'%s' % (self.image)
    
class Gallery(models.Model):
    galleryID  = models.AutoField(primary_key=True)
    gallery = models.CharField(max_length=255)
    galleryDescription = models.CharField(max_length=255)
    create_dt = models.DateField()
    edit_dt = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.gallaryID)

    def __str__(self):
        return u'%s' % (self.gallary)
    
class GalleryImage(models.Model):
    galleryImageID = models.AutoField(primary_key=True)
    imageID_fk = models.ForeignKey('Image', on_delete=models.CASCADE, )
    galleryID_fk = models.ForeignKey('Gallery', on_delete=models.CASCADE, )
    isCover = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.gallaryImageID)

    def __str__(self):
        return u'%s' % (self.gallaryImageID)
    