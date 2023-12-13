from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


from dominus.models import Organization
from .models import Player
from .forms import PlayerRegisterForm
# Create your views here.
class RegisterPlayerView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Player
    form_class = PlayerRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        #Lets check if the user can represent an Player? and has the rights to create a player magistrate.player.views line 21
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
        context["form_title"] = "Create Player"
        return context

class PlayerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Player
    form_class = PlayerRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Player.objects.get(id=self.kwargs.get("player_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the Player
        Player = self.get_object()
        return self.request.user == Player.creator or self.request.user in Player.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the Player after updating
        #can you look at this next line and correct it so ti goes to the detail view?
        
        return reverse_lazy('gladiatorus.player:playerDetailView', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Player"
        return context

class PlayerDetailView(DetailView):
    model = Player
    form_class = PlayerRegisterForm
    #template_name = 'path/to/your/detail_template.html'  # Specify your template here

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Player Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context

class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Player
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Player.objects.get(id=self.kwargs.get("player_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the Player
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Player"
        return context
    
def player_page(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    context = {
        'player': player,
        'form_title': 'Player Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'path/to/your/detail_template.html', context)