from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Job

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'second_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        # fields = '__all__'
        fields = ['name', 'description']
        # def get_queryset(self):
        #     return CustomUser.objects.filter(user=self.request.user)
