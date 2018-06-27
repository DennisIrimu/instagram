from django.test import TestCase
from .models import Image, Profile, Comments,followers,likes
from .django.contrib.auth.models import User
import datetime as dt
# Create your tests here.

class ProfileTestClass(TestCase):
    def setup(self):
        self.user= User(username='dnyt',email='lyricaldnyt@gmail.com',password='dimm8450')
        self.user.save()

        self.profile=Profile(profile_photo='/posts',bio='yadiyadi ya',profile_user=self.user,profile_follows="True")

    def test_instance(self):
        self.assertTrue(isinstance(self.bio,Profile,Profile))

    def test_save_method(self):
        self.bio.save_bio()
        profile =Profile.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(locations) == 0)

    def tearDown(self):
        Image.objects.all().delete()
