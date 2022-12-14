"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import UsersModelViewSet, UsersAPIView

from work.views import ProjectModelViewSet, TodoModelViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='librar',
        default_version='v1',
        description='Test api',
        contact=openapi.Contact(email='admin@gmail.com'),
        license=openapi.License(name='license'),
    ),
    public=True,
    # permission_classes=(Allowany)
)

router = DefaultRouter()

# router.register('users', UsersModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)
urlpatterns = [
    path('api-view/', UsersAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    # path('api-todo/', TodoAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('swagger<str:format>/', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/<str:version>/users/', UsersModelViewSet.as_view({'get': 'list'}))
]
