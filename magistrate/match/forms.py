from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Match

from datetimewidget.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper

class MatchRegisterForm(ModelForm):
    class Meta:
        model = Match
        fields = ["time",  "game", "attacker", "defender" ]

        widgets = {
                #Use localization and bootstrap 3
                'time': DateTimeWidget(attrs={'id':"time_id"}, usel10n = True, bootstrap_version=5),
                }
    def __init__(self, *args, **kwargs):
        super(MatchRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)