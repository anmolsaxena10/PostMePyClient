"""PostMePyClient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import *
from Auth.views import *
from Post.views import *
from Comment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login', login),
    path('do_login', do_login),
    path('register', register),
    path('do_register', do_register),
    path('ViewPost', view_post),
    path('add_comment', add_comment),
    path('do_add_comment', do_add_comment),
    path('logout', logout),
    path('delete_comment', delete_comment),
    path('add_post', add_post),
    path('do_add_post', do_add_post)
]
