from .models import Job
import django_filters

class JobFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Job
        fields = ['region', 'added']
