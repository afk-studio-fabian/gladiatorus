from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Profile

from crispy_forms.helper import FormHelper



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["profileImage"]
        #fields = [""]
    
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)