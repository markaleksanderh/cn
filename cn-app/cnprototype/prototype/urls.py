from django.urls import path
from . import views

from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
