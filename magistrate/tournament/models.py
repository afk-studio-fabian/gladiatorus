from django.db import models
import uuid

from django.contrib.auth.models import User

from dominus.models import Organization
from dominus.team.models import Team
from dominus.roster.models import Roster

from magistrate.game.models import Game
from magistrate.match.models import Match

from gladiatori.models import Player


# Create your models here.
class Tournament(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #long_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    FORMAT_CHOICES = [
        ('round_robin', 'Round Robin'),
        ('single_elimination', 'Single Elimination'),
        # ... add other formats as needed
    ]
    format = models.CharField(choices=FORMAT_CHOICES, max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tournaments')  # this references Django's User model
    registrar = models.ForeignKey(User,default=1, on_delete=models.CASCADE, related_name='registered_tournaments')  # this references Django's User model
    
    organization_host = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, related_name='hosted_tournaments')

    logo = models.ImageField(upload_to='user-uploads/tournaments/logos/', blank=True, null=True)
    banner = models.ImageField(upload_to='user-uploads/tournaments/banners/', blank=True, null=True)
    
    public = models.BooleanField(default=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='tournaments', default=1)
    #icon = logo
    # ... other tournament-related details ...
    def __str__(self):
        return self.name + " - " + self.format
    

class TournamentMatch(Match):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    # ... other tournament-match-related details ...
    def __str__(self):
        return self.tournament.name + " - " + self.attacker.name + " vs " + self.defender.name + " - " + self.game.name + " - " + str(self.time)
    # ... other tournament-match-related details ...

# class MatchSeries(models.Model):
#     team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
#     team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
#     tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
#     date_scheduled = models.DateTimeField()

    # ... other match series details ...

# class Round(models.Model):
#     match_series = models.ForeignKey(MatchSeries, on_delete=models.CASCADE, related_name='rounds')
#     round_number = models.PositiveIntegerField()
#     result = models.CharField(max_length=100)  # You can structure this as needed, maybe a JSON field if complex data
#     duration = models.DurationField()