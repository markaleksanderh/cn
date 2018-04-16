from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    num_jobs = Job.objects.all().count()
    job_list = Job.objects.all()
    return render(
    request,
    'index.html',
    context={'num_jobs': num_jobs, 'job_list': job_list},
    )
