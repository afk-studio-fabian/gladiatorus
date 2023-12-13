from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Tournament, TournamentMatch
from .forms import TournamentRegisterForm

# Create your views here.
class RegisterTournamentView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Tournament
    form_class = TournamentRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        #Lets check if the user can represent an Tournament? and has the rights to create a tournament magistrate.tournament.views line 21
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
        context["form_title"] = "Create Tournament"
        return context

class TournamentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tournament
    form_class = TournamentRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Tournament.objects.get(id=self.kwargs.get("tournament_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the Tournament
        Tournament = self.get_object()
        return self.request.user == Tournament.creator or self.request.user in Tournament.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the Tournament after updating
        #can you look at this next line and correct it so ti goes to the detail view?
        
        return reverse_lazy('magistrate.tournament:tournamentDetailView', kwargs={'tournament_id': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Tournament"
        return context

class TournamentDetailView(DetailView):
    model = Tournament
    form_class = TournamentRegisterForm
    #template_name = 'path/to/your/detail_template.html'  # Specify your template here
    def get_object(self, queryset=None):
        return Tournament.objects.get(id=self.kwargs.get("tournament_id"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Tournament Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context

class TournamentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tournament
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Tournament.objects.get(id=self.kwargs.get("tournament_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the Tournament
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Tournament"
        return context



def tournament_home(request, tournament_id):
    print("tournament_home")
    try:
        tournament = Tournament.objects.get(id=tournament_id)
    except Tournament.DoesNotExist:
        tournament = None
    
    
    

    context = {
        'page_title': tournament.name,
        'page_header': 'Tournament',
        'page_description': tournament.description,

        'tournament': tournament,
        'form_title': 'Tournament Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'tournament/tournament_app.html', context)


def tournament_page(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    context = {
        'tournament': tournament,
        'form_title': 'Tournament Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'tournament/tournament_app.html', context)

def tournament_match_page(request, tournament_id, match_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    match = get_object_or_404(TournamentMatch, id=match_id)
    context = {
        'tournament': tournament,
        'match': match,
        'form_title': 'Tournament Match Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'match/match_app.html', context)