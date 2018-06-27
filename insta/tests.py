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

class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(username='dnyt',email='lyricaldnyt@gmail.com',password='dimm8450')
        self.user.save()
        self.likes=likes(profile=self.user)
        self.likes.save()
        self.profile=Profile(profile_photo='/posts',bio='yadiyadi ya',profile_user=self.user)
        self.image=Image
        self.image.likes.add(self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.Image,Image))

    def test_save_image(self):
        self.image.save_image()
        images= Image.objets.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self):
        self.image.save_image()
        kwargs={'image':'/posts','image_name':'myname','image_caption':'myself'}
        Image.update_caption(self.inage.id,**kwargs)
        self.assertEqual("myname",self.image.image_name)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Imagge.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_get_image_id(self):
        image_id = id
        self.image.objects.get(pk=id)
        self.assertTrue(pk=id)

    def tearDown(self):
        Image.objects.all().delete()
