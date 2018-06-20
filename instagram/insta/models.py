from django.db import models
from djang.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='users',blank=True)

def __str__(self):
    return 'Profile for user {}'.format(self.user.username)
