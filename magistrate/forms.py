
from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Tournament

from crispy_forms.helper import FormHelper



# class TournamentRegisterForm(ModelForm):
#     class Meta:
#         model = Tournament
#         fields = ["name", "description", "start_date", "end_date", "format", "organization_host"]
#         #fields = [""]
    
#     def __init__(self, *args, **kwargs):
#         super(TournamentRegisterForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)