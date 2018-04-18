from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Job

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'second_name', 'username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class AddJobForm(forms.Form):
    class Meta:
        model = Job
        # fields = '__all__'
        fields = ['name', 'description', 'added', 'region']
