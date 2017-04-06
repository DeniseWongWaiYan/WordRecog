from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = ImageField(upload_to='users/%d/%m/%y', blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    
class photototesseractform(models.Model):
     user = Models.ForeignKey(Profile, related_name=images)   
     coverpic = models.ImageField(upload_to='user/%Y/%m/%d', blank=True, null=True)



