from django.shortcuts import render

from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User


from .models import Organization
from .forms import OrganizationRegisterForm

# Create your views here.


# Create your views here.
class RegisterOrganizationView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Organization
    form_class = OrganizationRegisterForm
    # def get_object(self, queryset=None):
    #     user = User.objects.get(id=self.kwargs.get("user_id"))
    #     return user.profile
    def test_func(self):
        return True
        #organization = self.get_object()
        #Lets check if the user can represent an organization? and has the rights to create a Organization magistrate.Organization.views line 21
        user_has_magistrate_orders = False
        user_has_magistrate_rights = False

        #Later 
        # user_has_magistrate_rights = user.magistrate.current.rights
        # user_has_magistrate_orders = user.magistrate.current.orders
        # 
        #

        user_is_apart_of_organization = self.is_user_apart_of_organization_owners()
        #user_is_apart_of_organization or
        user_is_owner = self.is_user_owner_of_organization()
        if user_is_owner or user_has_magistrate_orders or user_has_magistrate_rights:
            return True
        #return True
    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.registrar = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        # Find your next url here
        next_url = self.request.POST.get("next", None)
        return reverse('users:dashboard')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Register Organization"
        return context
    
    def is_user_apart_of_organization_owners(self):
        organization = self.get_object()
        user_is_apart_of_organization = False
        user_who_sent_the_request = self.request.user
        for account in organization.owners.all():
            if account == user_who_sent_the_request:
                user_is_apart_of_organization = True
                return True
        return False

    def is_user_owner_of_organization(self):
        organization = self.get_object()
        user_who_sent_the_request = self.request.user
        
        if organization.owner == user_who_sent_the_request:
            return True
        return False
        
    

class OrganizationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Organization
    form_class = OrganizationRegisterForm
    #template_name = 'path/to/your/detail_template.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context if needed
        context["form_title"] = "Team Details"
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        return context
    
    def test_func(self):
        # Assuming you want only the creator or owners to view the details
        organization = self.get_object()
        return self.request.user == organization.creator or self.request.user in organization.owners.all()






class OrganizationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Organization
    form_class = OrganizationRegisterForm
    #template_name = 'path/to/your/update_template.html'

    def get_object(self, queryset=None):
        return Organization.objects.get(id=self.kwargs.get("organization_id"))

    def test_func(self):
        # Assuming you want only the creator or owners to update the organization
        organization = self.get_object()
        return self.request.user == organization.creator or self.request.user in organization.owners.all()

    def get_success_url(self):
        # Redirect to the detail page of the organization after updating
        return reverse_lazy('name_of_organization_detail_view', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Update Organization"
        return context


class OrganizationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Organization
    #template_name = 'path/to/your/delete_template.html'

    def get_object(self, queryset=None):
        return Organization.objects.get(id=self.kwargs.get("organization_id"))
    def test_func(self):
        # Assuming you want only the creator to delete the organization
        return self.request.user == self.get_object().creator

    def get_success_url(self):
        # Redirect to a safe page, like user dashboard, after deletion
        return reverse_lazy('users:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context["form_title"] = "Delete Organization"
        return context






