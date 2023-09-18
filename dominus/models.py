from django.db import models
from gladiatori.models import Player
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='user-uploads/organizations/logos/', blank=True, null=True)
    founding_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owned_organization')

    # ... other organization-specific details ...

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Player, related_name='teams')
    team_logo = models.ImageField(upload_to='user-uploads/teams/logos/', blank=True, null=True)
    formation_date = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teams')

    # ... other team-related details ...

class TeamOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner_profile')
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='user-uploads/owners/avatars/', blank=True, null=True)

    # ... other owner-specific details ...