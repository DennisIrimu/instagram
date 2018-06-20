from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL)
    profile_photo = models.ImageField(upload_to='users',blank=True)
    bio = models.CharField(max_length=60)
    profile_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    
def __str__(self):
    return 'Profile for user {}'.format(self.user.username)
