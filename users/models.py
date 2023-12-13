from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
import uuid

from users.orientation.models import Orientation

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    profileImage = models.ImageField(null=True, blank=True, default="server_essentials/tmp_user_icon.png", upload_to="user_uploads/profile/profile_images")


    allowed_orientations = models.ManyToManyField(Orientation, related_name='users_allowed')
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
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return self.user.username


class Styling(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    themeStyle = models.CharField(default="light", max_length=16)
    canvasStyle = models.CharField(default="clean", max_length=16)
    display_canvasNoise = models.BooleanField(default=False)


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        print("FOUND Style")
        try:
            instance.styling.save()
        except ObjectDoesNotExist:
            Styling.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.styling.save()

    def __str__(self):
        return "Styling - " + self.user.username
    
