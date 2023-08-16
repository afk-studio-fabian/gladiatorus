from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, SelectDateWidget, TextInput, widgets
from .models import Profile




class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["profileImage"]
        #fields = [""]