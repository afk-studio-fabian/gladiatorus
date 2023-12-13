
from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Organization

from datetimewidget.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper



class OrganizationRegisterForm(ModelForm):
    class Meta:
        model = Organization
        fields = ["name", "logo", "description", "owners",]

    
    def __init__(self, *args, **kwargs):
        super(OrganizationRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


