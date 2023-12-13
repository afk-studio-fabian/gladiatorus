from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


from dominus.models import Organization
from .models import Team
from .forms import TeamRegisterForm
# Create your views here.


class RegisterTeamView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Team
    form_class = TeamRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        #Lets check if the user can represent an Team? and has the rights to create a team dominus.team.views line 21
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
        context["form_title"] = "Create Team"
        return context

class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    form_class = TeamRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Team.objects.get(id=self.kwargs.get("team_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the Team
        Team = self.get_object()
        return self.request.user == Team.creator or self.request.user in Team.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the Team after updating
        #can you look at this next line and correct it so ti goes to the detail view?
        
        return reverse_lazy('dominus.team:teamDetailView', kwargs={'team_id':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Team"
        return context

class TeamDetailView(DetailView):
    model = Team
    form_class = TeamRegisterForm
    #template_name = 'path/to/your/detail_template.html'  # Specify your template here

    def get_object(self, queryset=None):
        return Team.objects.get(id=self.kwargs.get("team_id"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Team Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context

class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Team.objects.get(id=self.kwargs.get("team_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the Team
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Team"
        return context
    
def team_home(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    context = {
        'team': team,
        'form_title': 'Team Details',
        'previous_page': request.META.get('HTTP_REFERER'),
    }
    return render(request, 'team/team_app.html', context)




