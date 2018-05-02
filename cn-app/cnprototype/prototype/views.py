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
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AddJob(LoginRequiredMixin, generic.CreateView):
    login_url = '/prototype/login/'
    # login_url = 'accounts/login/'
    # redirect_field_name = 'redirect_to'
    form_class = AddJobForm
    success_url = reverse_lazy('view_jobs')
    template_name = 'add_job.html'
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(AddJob, self).form_valid(form)
    # def get_queryset(self):
    #     return CustomUser.objects.filter(user=self.request.user)

class UpdateJob(LoginRequiredMixin, generic.UpdateView):
    model = Job
    fields = ['description']
    template_name_suffix = '_update_form'


class ViewJobs(LoginRequiredMixin, generic.ListView):
    login_url = '/prototype/login/'
    template_name = 'view_jobs.html'
    # redirect_field_name = 'redirect_to'
    # permission_denied_message = 'You must be logged-in to view this content'

    def get(self, request, *args, **kwargs):
        user = self.request.user.id
        job_list = Job.objects.exclude(added_by__exact=user)
        return render(request, self.template_name, {'job_list': job_list})


class Dashboard(generic.DetailView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        user = self.request.user
        job_list = Job.objects.filter(added_by__exact=user.id)
        return render(request, self.template_name, {'job_list': job_list}, {'user': user})


class JobDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/prototype/login/'
    model = Job
    template_name = 'job_detail.html'
    def get(self, request, *args, **kwargs):
        user = self.request.user
        job = Job.objects.get(pk=self.kwargs.get('pk'))
        return render(request, self.template_name, {'job': job}, {'user': user})




# class ViewUser(generic.TemplateView):
#     template_name = "view_user.html"
#     context_object_name = user_profile
