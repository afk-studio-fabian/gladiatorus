from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Roster

from datetimewidget.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper



class RosterRegisterForm(ModelForm):
    class Meta:
        model = Roster
        fields = ["name", "tag", "team", "players", "game", "organization"]

    
    def __init__(self, *args, **kwargs):
        super(RosterRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)