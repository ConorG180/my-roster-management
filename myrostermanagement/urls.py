"""myrostermanagement URL Configuration

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
from django.urls import path
from roles.views import role, add_role, edit_role
from home.views import home
from employees.views import employee
from workshifts.views import workshift

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('role/', role, name="role_table"),
    path('add-role/', add_role, name="add_role"),
    path('add-role/add', add_role, name="add_role"),
    path('edit-role/<role_id>', edit_role, name="edit"),
    path('employee/', employee, name="employee"),
    path('workshift/', workshift, name="workshift"),
]