from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Match
from .forms import MatchRegisterForm
from magistrate.tournament.models import TournamentMatch

# Create your views here.
class RegisterMatchView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Match
    form_class = MatchRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        #Lets check if the user can represent an Match? and has the rights to create a match magistrate.match.views line 21
        return True
    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.registrar = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        # Find your next url here
        next_url = self.request.POST.get("next", None)
        return reverse('users:dashboard')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Create Match"
        return context


#Can we have this class check if the match is a tournament match or a standalone match?
# If it is a tournament match, let's include the tournament match model
# If it is a standalone match, let's include the standalone match model

class MatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Match
    form_class = MatchRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Match.objects.get(id=self.kwargs.get("match_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the Match
        Match = self.get_object()
        return self.request.user == Match.creator or self.request.user in Match.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the Match after updating
        #can you look at this next line and correct it so ti goes to the detail view?
        
        return reverse_lazy('magistrate.match:matchDetailView', kwargs={'match_id': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Match"
        return context

class MatchDetailView(DetailView):
    model = Match
    form_class = MatchRegisterForm
    #template_name = 'path/to/your/detail_template.html'  # Specify your template here

    def get_object(self, queryset=None):
        return Match.objects.get(id=self.kwargs.get("match_id"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Match Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context

class MatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Match
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Match.objects.get(id=self.kwargs.get("match_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the Match
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Match"
        return context
    
def match_home(request, match_id):
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        match = None
    
    try:
        tournamentMatch = TournamentMatch.objects.get(id=match_id)
        match = tournamentMatch
    except TournamentMatch.DoesNotExist:
        tournamentMatch = None
    print(tournamentMatch)
    
    if tournamentMatch:
        pass
        #match = tournamentMatch
    
    description = match.attacker.name + " vs " + match.defender.name + " - " + str(match.time) + " - " + match.game.name    
    context = {
        'page_title': 'Match: ' + match.attacker.tag + " vs " + match.defender.tag  + " - " + str(match.time) + " - " + match.game.name,
        'page_header': 'Tournament',
        'page_description': description,

        'match': match,
        #'tournament' = tour
        
        'form_title': 'Match Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'match/match_app.html', context)