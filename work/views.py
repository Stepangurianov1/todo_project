from django.http import Http404
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status

from .filte import ProjectFilter, TodoFilter
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet, LimitOffsetPagination):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    # filterset_fields = ['project']
    filterset_class = TodoFilter
    pagination_class = TodoLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

# class TodoAPIView(APIView):
#     def get(self, request, format=None):
#         todo_id = request.query_params.get('pk')
#         todo_list = Todo.objects.all()
#         if todo_id:
#             todo_list = Todo.objects.filter(id=todo_id)
#         serializer = TodoModelSerializer(todo_list, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TodoModelSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     def delete(self, request, format=None):
#         todo_id = request.query_params.get('pk')
#         todo_obj = Todo.objects.get(id=todo_id)
#         todo_obj.is_active = False
#         todo_obj.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
