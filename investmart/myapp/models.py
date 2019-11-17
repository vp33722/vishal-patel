from django.db import models
# Create your models here.

#Main "myapp" table which will contain title and description
class myapp(models.Model):
    title = models.CharField(max_length=100,default=' ')
    description = models.CharField(max_length=100000,default=' ')
    longitude=models.CharField(max_length=1000,default=0)
    latitude=models.CharField(max_length=1000,default=0)
    placetitle=models.CharField(max_length=100000,default= ' ',blank = True)
    placetitle2=models.CharField(max_length=100000,default=' ',blank = True)
    placetitle3=models.CharField(max_length=100000,default=' ',blank = True)
    placetitle4=models.CharField(max_length=100000,default=' ',blank = True)
    placevalue=models.CharField(max_length=100000,default=' ',blank = True)
    placevalue2=models.CharField(max_length=100000,default=' ',blank = True)
    placevalue3=models.CharField(max_length=100000,default=' ',blank = True)
    placevalue4=models.CharField(max_length=100000,default=' ',blank = True)
    
    class Meta:
        db_table = 'placeDb'

    def __str__(self):
        return self.title

#"imageLoc" Table which will store place_id frm "myapp" table and image with its status 
class imageLoc(models.Model):
    place_id = models.IntegerField()
    imageLocation = models.FileField(upload_to="images/",default=' ',blank = False)
    status = models.CharField(max_length = 1000 , default = " ")

    class Meta:
        db_table = 'imageDb'

    def __str__(self):
        return self.imageLocation

    #for ddleteing data from the file system
    def delete(self, *args, **kwargs):
        self.imageLocation.delete()
        super().delete(*args, **kwargs)


#"videoLoc" Table which will store place_id frm "myapp" table and video with its status 
class VideoLoc(models.Model):
    place_id = models.IntegerField()
    vedioLocation = models.FileField(upload_to="vedios/",default=' ',blank = False)
    status = models.CharField(max_length = 1000 , default = " ")

    class Meta:
        db_table = 'vedioDb'

    def __str__(self):
        return self.vedioLocation

    #for ddleteing data from the file system
    def delete(self, *args, **kwargs):
        self.vedioLocation.delete()
        super().delete(*args, **kwargs)
#description table will store place id from myapp
class Description(models.Model):
    place_id=models.IntegerField()
    descriptionPlace=models.CharField(max_length=100000)
    status=models.BooleanField(default=False)
    class Meta:
        db_table = 'description'

    def __str__(self):
        return self.descriptionPlace
    def delete(self, *args, **kwargs):
        self.descriptionPlace.delete()
        super().delete(*args, **kwargs)