from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='user-uploads/games/logos/', blank=True, null=True)
    banner = models.ImageField(upload_to='user-uploads/games/banners/', blank=True, null=True)
    
    # ... other game-related details ...

    def __str__(self):
        return self.name