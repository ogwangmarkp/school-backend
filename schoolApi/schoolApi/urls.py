"""
URL configuration for schoolApiApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school import views as school_views
from staff import views as staff_views
from student import views as student_views

router = DefaultRouter()  

router.register(r'schools', school_views.SchoolView, basename='school')
router.register(r'staff', staff_views.StaffView, basename='staff')
router.register(r'student', student_views.StudentsView, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
