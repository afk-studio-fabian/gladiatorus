from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Game

from datetimewidget.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper

class GameRegisterForm(ModelForm):
    class Meta:
        model = Game
        fields = ["name",  "description", "logo", "banner" ]

    
    def __init__(self, *args, **kwargs):
        super(GameRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)