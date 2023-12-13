from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timedelta
import uuid


# STATIC IMPORTS


# # Create your models here.
# class Orientation(models.Model):
#     ROLE_CHOICES = (
#         ('player', 'Player'),
#         ('team', 'Team'),
#         ('organizer', 'Organizer'),
#         ('developer', 'Developer'),
#         # Add more roles as needed
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=100, choices=ROLE_CHOICES)
#     # other fields to store orientation-specific data or preferences
    
#     # example of storing graphical assets
#     icon = models.ImageField(upload_to='orientation_icons/')
    
#     def __str__(self):
#         return f'{self.user.username} - {self.role}'


class Orientation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    banner_image = models.ImageField(upload_to='users/orientation/orientation_banners/user_uploads/', default='users/orientation/orientation_banners/default/default_banner.png')
    icon = models.ImageField(upload_to='users/orientation/orientation_icons/user_uploads/', default='users/orientation/orientation_icons/default/default_1000.png')
    

    def save(self, *args, **kwargs):
        if not self.name:  # Only set name if it's not set already.
            self.name = f"New Orientation - {uuid.uuid4()}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    

class UserOrientation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    

    def get_template(self):
        print("ME GETS TEMPLATE - user.orientation.models")
        if self.orientation.name.lower() in ['magistrate', 'dominus', 'gladiatorus']:
            return f'components/core/gmm-core/gmm-core-{self.orientation.name.lower()}.html'
        else:
            print(self.orientation.name.lower())
            return 'components/core/gmm-core/gmm-core-template.html'
    
    def __str__(self):
        return f'{self.user.username} - {self.orientation.name}'
    
# class UserAllowedOrientations(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     orientations = models.ManyToManyField(Orientation,related_name='users_allowed')
    
#     def __str__(self):
#         return f'{self.user.username} - {self.orientations}'

class UserOrientationTracker(models.Model):
    user_orientation = models.ForeignKey(UserOrientation, on_delete=models.CASCADE)
    last_session_start = models.DateTimeField(auto_now_add=True)
    last_session_end = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.DurationField(default=timedelta())
    current = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user_orientation} - Last Session: {self.last_session_start} to {self.last_session_end} - Total: {self.total_time_spent}'

class UserOrientationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_orientation = models.ForeignKey(Orientation, related_name='from_orientation', on_delete=models.CASCADE)
    to_orientation = models.ForeignKey(Orientation, related_name='to_orientation', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.from_orientation} to {self.to_orientation} at {self.timestamp}'