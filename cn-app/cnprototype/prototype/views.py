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

from django.shortcuts import render

from django.http import HttpResponse

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
    template_name = 'view_jobs.html'
    def get(self, request, *args, **kwargs):
        user = self.request.user.id
        job_list = Job.objects.exclude(added_by__exact=user)
        return render(request, self.template_name, {'job_list': job_list})


class Dashboard(generic.TemplateView):
    template_name = 'index.html'
    context_object_name = 'user_profile'
    def get_queryset(self):
        return CustomUser.objects.filter(user=self.request.user)

class JobDetail(generic.DetailView):
    model = Job




# class ViewUser(generic.TemplateView):
#     template_name = "view_user.html"
#     context_object_name = user_profile
