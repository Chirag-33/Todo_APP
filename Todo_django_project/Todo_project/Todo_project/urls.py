"""
URL configuration for Todo_project project.

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
from Todo.views import home,register,user_login,add_task,task_list,user_logout,delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout , name='logout'),
    path('add_task', add_task , name='add_task'),
    path('task_list', task_list , name='task_list'),
    path('delete_task/<int:id>/',delete_task, name='delete_task')
]
