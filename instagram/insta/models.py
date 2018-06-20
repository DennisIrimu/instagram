from django.db import models
from django.conf import settings
import datetime as dt
# Create your models here.
class Profile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL)
    profile_photo = models.ImageField(upload_to='users',blank=True)
    bio = models.CharField(max_length=60)
    #profile_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


def __str__(self):
    return 'Profile for user {}'.format(self.user.username)

class Image(models.Model):

    image=models.ImageField(upload_to = 'posts/',blank=True)
    image_name=models.CharField(max_length=60)
    image_caption=models.CharField(max_length=60)
    image_profile=models.ForeignKey(Profile,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    #likes=models.ManyToManyField(User,related_name="likes",default=None)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.image_name
