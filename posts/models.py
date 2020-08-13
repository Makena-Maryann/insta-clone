from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/',blank=True,null=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    caption = models.TextField()
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,) 
    date_posted = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images 
    
    @classmethod
    def search_by_caption(cls,search_term):
        post = cls.objects.filter(caption__icontains=search_term)
        return post
    
    def __str__(self):
        return self.image_name