from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Job, Company, Region, Quote

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'name']

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Region)
admin.site.register(Quote)
