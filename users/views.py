from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User

from users.forms import CustomUserCreationForm, ProfileEditForm

from .models import Profile


def dashboard(request):
    context = {"page_title":"Bruker"}
    return render(request, "users/dashboard.html", context)

def register(request):
    if request.method =="GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("GODKJENT")
            return redirect(reverse("users:dashboard"))
        else:
            #print(form.errors)
            print("AVKREFTET - bug i register funksjon")
            return render(
            request, "users/register.html",
            {"form": form}
        )

def setup_profile(request):
    form = True
    if request.method =="GET":
        return render(request, "users/profile_setup.html", {"form":form})
    elif request.method =="POST":
        if form: #form.is_valid
            return redirect(reverse("users:dashboard"))
        else:
            return render(request, "users/profile_setup.html", {"form":form})





class updateProfileView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    def get_object(self, queryset=None):
        user = User.objects.get(id=self.kwargs.get("user_id"))
        return user.profile
    def test_func(self):
        profile = self.get_object(self)
        if self.request.user.id == profile.user.id:
            return True
        print("FALSE")
        return False
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        # Find your next url here
        next_url = self.request.POST.get("next", None)
        return reverse('users:dashboard')