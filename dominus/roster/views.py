from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


from dominus.models import Organization
from .models import Roster
from .forms import RosterRegisterForm

# Create your views here.
### --- Roster --- ###
class RegisterRosterView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Roster
    form_class = RosterRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        #Lets check if the user can represent an Roster? and has the rights to create a roster dominus.roster.views line 21
        #Can we check if the banner has actually been uploaded?
        
        
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
        context["form_title"] = "Create Roster"
        return context

class RosterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Roster
    form_class = RosterRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Roster.objects.get(id=self.kwargs.get("roster_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the Roster
        Roster = self.get_object()
        return self.request.user == Roster.creator or self.request.user in Roster.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the Roster after updating
        #can you look at this next line and correct it so ti goes to the detail view?
        
        return reverse_lazy('dominus.roster:rosterDetailView', kwargs={'roster_id':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Roster"
        return context

class RosterDetailView(DetailView):
    model = Roster
    form_class = RosterRegisterForm
    #template_name = 'path/to/your/detail_template.html'  # Specify your template here

    def get_object(self, queryset=None):
        return Roster.objects.get(id=self.kwargs.get("roster_id"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Roster Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context

class RosterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Roster
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Roster.objects.get(id=self.kwargs.get("roster_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the Roster
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Roster"
        return context