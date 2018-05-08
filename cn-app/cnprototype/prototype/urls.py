# from django.urls import path
# from . import views
#
# from django.contrib import admin
# from django.urls import include
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
#
# # login at http://localhost:8000/prototype/accounts/login/
#
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('add_job/', views.AddJob.as_view(), name='add_job'),
    path('view_jobs/', views.ViewJobs.as_view(), name='view_jobs'),
    # path('', views.Dashboard.as_view(), name='dashboard'),
    path('job/<int:pk>', views.JobDetail.as_view(), name='job_detail'),
    path('job/<int:pk>/add_quote', views.AddQuote.as_view(), name='add_quote'),
    path('quote/<int:pk>', views.QuoteDetail.as_view(), name='quote_detail'),
]
