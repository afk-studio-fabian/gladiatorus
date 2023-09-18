from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Styling



# when a user is saved then send this signal.
# the signal is received by the receiver, which is the create_profile function.
# saves the profile object everytime it is "saved".
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("FOUND USER")
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
    try:
        instance.styling.save()
    except ObjectDoesNotExist:
        Styling.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):

    instance.profile.save()
    instance.styling.save()