from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import MyUsers

UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
admin.site.register(MyUsers, UserAdmin)

