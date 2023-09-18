from django.db import models
from gladiatori.models import Player
from django.contrib.auth.models import User
from dominus.models import Team, Organization

# Create your models here.
class Tournament(models.Model):
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
    organization_host = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, related_name='hosted_tournaments')

    # ... other tournament-related details ...

class MatchSeries(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    date_scheduled = models.DateTimeField()

    # ... other match series details ...

class Round(models.Model):
    match_series = models.ForeignKey(MatchSeries, on_delete=models.CASCADE, related_name='rounds')
    round_number = models.PositiveIntegerField()
    result = models.CharField(max_length=100)  # You can structure this as needed, maybe a JSON field if complex data
    duration = models.DurationField()

    # ... other round-specific details ...