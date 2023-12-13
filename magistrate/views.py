from django.shortcuts import render

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User

#from .models import Tournament
#from .forms import TournamentRegisterForm

# Create your views here.
# class RegisterTournamentView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
#     model = Tournament
#     form_class = TournamentRegisterForm
#     # def get_object(self, queryset=None):
#     #     user = User.objects.get(id=self.kwargs.get("user_id"))
#     #     return user.profile
#     def test_func(self):
#         #Lets check if the user can represent an organization? and has the rights to create a tournament magistrate.tournament.views line 21
#         return True
#     def form_valid(self, form):
#         form.instance.creator = self.request.user
#         form.instance.registrar = self.request.user
#         return super().form_valid(form)
#     def get_success_url(self):
#         # Find your next url here
#         next_url = self.request.POST.get("next", None)
#         return reverse('users:dashboard')