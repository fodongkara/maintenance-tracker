"""maintenance_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from auth.views import UserViewSet, UserRegisterViewSet
from maintainance_requests.views import MaintainanceRequestViewSet
from rest_framework_jwt.views import obtain_jwt_token



router = DefaultRouter()
router.register('api/v1/auth/register', UserRegisterViewSet)
router.register('api/v1/users', UserViewSet)
router.register('api/v1/requests', MaintainanceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/auth/signin/', obtain_jwt_token),
]
