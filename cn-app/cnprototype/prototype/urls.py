from django.urls import path
from . import views

from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]

# login at http://localhost:8000/prototype/accounts/login/

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
