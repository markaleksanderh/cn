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
    # current_user = lambda self: CustomUser.objects.filter(user=self.request.user.id)
    # model = Job
    # context_object_name = 'job_list'
    template_name = 'view_jobs.html'
    # queryset = Job.objects.order_by('-added')
    # queryset = Job.objects.order_by('-added').exclude(added_by__exact=6)
    # def get(self, request):
    #     user = self.request.user.id
    #     job_list = Job.objects.filter(added_by__exact=n_user)
    #     return HttpResponse(job_list)
    # queryset = queryset.exclude(added_by__exact=6)

    # paginate_by = 5
    #


    # n_user = lambda self : self.request.user.id
    # queryset = Job.objects.filter(added_by__exact=n_user)
    # template_name = 'view_jobs.html'



    def get(self, request, *args, **kwargs):
        user = self.request.user.id
        job_list = Job.objects.exclude(added_by__exact=user)
        # return HttpResponse(job_list)
        return render(request, self.template_name, {'job_list': job_list})





    # def get_queryset(self, request):
    #     user = self.request.user.id
    #     job_list = Job.objects.filter(added_by__exact=user)
    #     return job_list

    # def get_queryset(self, request):
    #     user = self.request.user.id
    #     job_list = Job.objects.exclude(added_by__exact=user)
    #     return job_list

    # def get_queryset(self):
    #     current_user = CustomUser.objects.filter(user=self.request.user)
    #     job_list = Job.objects.all()
    #     return job_list
    # def get_queryset(self):
    #     return CustomUser.objects.filter(user=self.request.user)

class Dashboard(generic.TemplateView):
    template_name = 'index.html'
    context_object_name = 'user_profile'
    def get_queryset(self):
        return CustomUser.objects.filter(user=self.request.user)

class JobDetail(generic.DetailView):
    model = Job
    # template_name = 'job_detail.html'
    # context_object_name = 'job_detail'
    # queryset = Job.objects.get(pk=id)
    # queryset = Job.objects.all()



# class ViewUser(generic.TemplateView):
#     template_name = "view_user.html"
#     context_object_name = user_profile
