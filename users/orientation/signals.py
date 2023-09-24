from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Orientation, UserOrientation

@receiver(post_save, sender=User)
def create_user_orientation(sender, instance, created, **kwargs):
    if created:
        default_orientation = Orientation.objects.get(name='Novice')  # or another default
        UserOrientation.objects.create(user=instance, orientation=default_orientation)
