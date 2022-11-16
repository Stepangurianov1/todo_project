from django_filters import rest_framework as filters

from work.models import Project, Todo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    data = filters.DateFilter()
    data__gt = filters.DateFilter(field_name='data', lookup_expr='gt')
    data__lt = filters.DateFilter(field_name='data', lookup_expr='lt')

    class Meta:
        model = Todo
        fields = ['project', 'data']
