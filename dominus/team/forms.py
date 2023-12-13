from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Team

from datetimewidget.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper

class TeamRegisterForm(ModelForm):
    class Meta:
        model = Team
        fields = ["name", "tag", "members", "logo", "banner", "description", "organization"]

    
    def __init__(self, *args, **kwargs):
        super(TeamRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


