from django.db import models
from dominus.team.models import Team
from gladiatori.models import Player
from magistrate.game.models import Game
from dominus.models import Organization

# Create your models here.
class Roster(models.Model):
    #one team can have many rosters, and a roster can only have one team 
    name = models.CharField(max_length=100, default="Roster Name")
    tag = models.CharField(max_length=10, default="Roster Tag")

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='roster')
    #player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='roster')
    players = models.ManyToManyField(Player, related_name='rosters')
    # ... other roster-related details ...
    
    #game = models.CharField(max_length=100, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='roster', null=True, blank=True)
    
    #formation_date = models.DateTimeField(auto_now_add=True)
    #founding_date = models.DateTimeField(auto_now_add=True)
    #creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_rosters", null=True, blank=True)
    #registrar = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="registered_rosters", null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='rosters', default=1)
    
    def __str__(self):
        return self.team.name + " - " +self.name + " (" +  self.tag + ") - " + self.game.name