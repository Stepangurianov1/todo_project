from django.db import models

# Create your models here.
from django.utils.timezone import now
from users.models import Users


class ObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


class Project(models.Model):
    objects = ObjectsManager
    name = models.URLField(max_length=128, blank=True, null=True)
    users = models.ManyToManyField(Users)
    def __str__(self):
        return f'ссылка на проект - {self.name}'


class Todo(models.Model):
    objects = ObjectsManager
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    data_create = models.DateField(auto_now_add=True)
    data_update = models.DateField(auto_now=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

