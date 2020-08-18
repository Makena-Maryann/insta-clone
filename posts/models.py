from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='pics/',default='default.jpg')
    bio = HTMLField(blank=True,default='I am a new user!')
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save()
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    caption = HTMLField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images 
    
    @classmethod
    def search_by_caption(cls,search_term):
        post = cls.objects.filter(caption__icontains=search_term)
        return post

    @classmethod
    def filter_images_by_user(cls,id):
        images_by_user = cls.objects.filter(profile = id).all() 
        return images_by_user    
    
    def __str__(self):
        return self.image_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey('Image',on_delete=models.CASCADE)
    content = HTMLField()
    date_posted = models.DateTimeField(auto_now_add=True)   

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image_id=id)
        return comments     

   