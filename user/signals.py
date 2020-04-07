# This program is for signaling once user is created,create a profile for him

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile

'''
when user is saved, it sends a signal which is received by @receiver.
@receiver is  createProfile function 
which create an object with the user instance
'''


@receiver(post_save, sender=User)
def createProfile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


''' once the Profile is created it sends another signal to save profile '''


@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()
