"""mold URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import communication.views
import account.views
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.home, name="home"),
    path('mypage/', communication.views.mypage, name="mypage"),
    path('template/', communication.views.template, name="template"),
    path('grade/', communication.views.grade, name="grade"),
    path('creategrade/', communication.views.creategrade, name="creategrade"),
    path('meeting/', communication.views.meeting, name="meeting"),
    path('createmeeting/', communication.views.createmeeting, name="createmeeting"),
    path('attendance/', communication.views.attendance, name="attendance"),
    path('createattendance/', communication.views.createattendance, name="createattendance"),
    path('recommendation/', communication.views.recommendation, name="recommendation"),
    path('createrecommendation/', communication.views.createrecommendation, name="createrecommendation"),
    path('account/login', account.views.login_view, name="login"),
    path('account/logout', account.views.logout_view, name="logout"),
    path('account/register', account.views.register_view, name="register"),
    path('community/communityhome/', community.views.communityhome, name="communityhome"),
    path('community/new/', community.views.new, name="new"),
    path('community/create/', community.views.create, name="create"),
    path('community/detail/<int:community_id>', community.views.detail, name="detail"),
    path('community/newreply/<int:community_id>', community.views.newreply, name="newreply"),
    path('community/edit/<int:community_id>', community.views.edit, name="edit"),
    path('community/update/<int:community_id>', community.views.update, name="update"),
    path('community/delete/<int:community_id>', community.views.delete, name="delete"),
    path('community/deletereply/<int:community_id>/<int:reply_id>', community.views.deletereply, name="deletereply"),
    path('article/', communication.views.mypage1, name="article"),
    path('write/',community.views.communityhome1, name="write"),
]
