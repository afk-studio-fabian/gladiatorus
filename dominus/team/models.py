from django.db import models
from gladiatori.models import Player
from dominus.models import Organization
from django.contrib.auth.models import User

from magistrate.game.models import Game


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, default="Team Name")
    tag = models.CharField(max_length=10, default="Team Tag")
    members = models.ManyToManyField(Player, related_name='teams')
    logo = models.ImageField(upload_to='user-uploads/teams/logos/', blank=True, null=True)
    description = models.TextField(blank=True)
    
    
    #A banner with specific dimensions here  # Can we add a dimenstion check to the banner?  

    banner = models.ImageField(upload_to='user-uploads/teams/banners/', blank=True, null=True)

    #Banner is not working, can we write a test to see if the banner actually has been uploaded and added to the model?



    formation_date = models.DateTimeField(auto_now_add=True)
    founding_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_teams", null=True, blank=True)
    registrar = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="registered_teams", null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teams')

    # ... other team-related details ...

    def __str__(self):
        return self.name
    

   


    