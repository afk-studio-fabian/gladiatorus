from django.db import models
import uuid
from django.contrib.auth.models import User
from magistrate.game.models import Game
from dominus.team.models import Team

# Create your models here.

class Match(models.Model):
    #id = models.UUIDField(_(""), primary_key=True, default=uuid.uuid4, editable=False)"))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    creator = models.ForeignKey(User,default=1, on_delete=models.CASCADE, related_name='created_matches')  # this references Django's User model
    registrar = models.ForeignKey(User,default=1, on_delete=models.CASCADE, related_name='registered_matches')  # this references Django's User model

    # Static information
    time = models.DateTimeField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='matches')

    # Dynamic information

    #teams/rosters
    attacker = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='attacker_matches')
    defender = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='defender_matches') 


    def __str__(self):
        return self.attacker.name + " vs " + self.defender.name + " - " + self.game.name
    

class StandaloneMatch(Match):
    # ... other match-related details ...
    logo = models.ImageField(upload_to='user-uploads/matches/logos/', blank=True, null=True)
    def __str__(self):
        return self.attacker.name + " vs " + self.defender.name + " - " + self.game.name
    # ... other match-related details ...

# Maybe we can have a model that relates the attacker and the defender to the match 
# class defender(models.Model):
#     match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='defender_matches')
#     defender = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='defender_matches')
#     # ... other roster-related details ...
#     score = models.IntegerField(default=0)

