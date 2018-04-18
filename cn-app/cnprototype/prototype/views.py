# from django.shortcuts import render
# from .models import Job
#
# # Create your views here.
# def index(request):
#     num_jobs = Job.objects.all().count()
#     job_list = Job.objects.all()
#     return render(
#     request,
#     'index.html',
#     context={'num_jobs': num_jobs, 'job_list': job_list},
#     )


# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponse

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AddJob(generic.TemplateView):
    template_name = "add_job.html"

class ViewJobs(generic.ListView):
    model = Job
    context_object_name = 'job_list'
    queryset = Job.objects.all()
    template_name = "view_jobs.html"
    # def get(self, request):
    #     return HttpResponse('View jobs')
