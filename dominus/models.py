from django.db import models
from gladiatori.models import Player
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='user-uploads/organizations/logos/', blank=True, null=True)
    founding_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_organizations", null=True, blank=True)
    registrar = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="registered_organizations", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="owner_organization", null=True, blank=True)
    
    #owner = models.CharField(max_length=150)

    #owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner_organization', default=1)
    #creator = models.OneToOneField(User, on_delete=models.CASCADE, related_name='created_organization', default=1)
    #registrar = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registered_organization', default=1)
    owners = models.ManyToManyField(User, related_name="owned_organizations", blank=True)

    
    def __str__(self):
        return str(self.name) +" - " + str(self.owner)
    # ... other organization-specific details ...


class TeamOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner_profile')
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='user-uploads/owners/avatars/', blank=True, null=True)

    # ... other owner-specific details ...