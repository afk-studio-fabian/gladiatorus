from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Game
from .forms import GameRegisterForm

# Create your views here.
class RegisterGameView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Game
    form_class = GameRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        #Lets check if the user can represent an Game? and has the rights to create a game magistrate.game.views line 21
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
        context["form_title"] = "Create Game"
        return context

class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Game.objects.get(id=self.kwargs.get("game_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the Game
        Game = self.get_object()
        return self.request.user == Game.creator or self.request.user in Game.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the Game after updating
        #can you look at this next line and correct it so ti goes to the detail view?
        
        return reverse_lazy('magistrate.game:gameDetailView', kwargs={'game_id': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Game"
        return context

class GameDetailView(DetailView):
    model = Game
    form_class = GameRegisterForm
    #template_name = 'path/to/your/detail_template.html'  # Specify your template here

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Game Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Game.objects.get(id=self.kwargs.get("game_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the Game
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Game"
        return context
    
def game_page(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    context = {
        'game': game,
        'form_title': 'Game Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'path/to/your/detail_template.html', context)