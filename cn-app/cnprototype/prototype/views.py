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
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Job

# from django.http import HttpResponse

from .forms import CustomUserCreationForm
from .forms import AddJobForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AddJob(generic.CreateView):
    form_class = AddJobForm
    success_url = reverse_lazy('view_jobs')
    template_name = 'add_job.html'
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(AddJob, self).form_valid(form)
    # def get_queryset(self):
    #     return CustomUser.objects.filter(user=self.request.user)

class ViewJobs(generic.ListView):
    model = Job
    context_object_name = 'job_list'
    queryset = Job.objects.all()
    template_name = 'view_jobs.html'
    pagine_by = 2
    # def get(self, request):
    #     return HttpResponse('View jobs')

class Dashboard(generic.TemplateView):
    template_name = "index.html"
    context_object_name = 'user_profile'
    def get_queryset(self):
        return CustomUser.objects.filter(user=self.request.user)
