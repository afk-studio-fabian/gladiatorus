from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# If you use Django's built-in User model for authentication, or a custom user model

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    handle = models.CharField(max_length=100) # Add handle check function
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='players/avatars/', blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=1000)  # Elo, MMR, or any other rating system you might use
    
    # ... any other player-specific details ...

    def __str__(self):
        return self.handle