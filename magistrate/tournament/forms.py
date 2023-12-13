
from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Tournament

from datetimewidget.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper



class TournamentRegisterForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ["name", "description", "start_date", "end_date", "format", "organization_host", "logo", "banner" ,"public", "game"]
        #fields = [""]

        widgets = {
            #Use localization and bootstrap 3
            'start_date': DateTimeWidget(attrs={'id':"start_date_id"}, usel10n = True, bootstrap_version=5),
            'end_date': DateTimeWidget(attrs={'id':"end_date"}, usel10n = True, bootstrap_version=5)
        }
    
    def __init__(self, *args, **kwargs):
        super(TournamentRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)