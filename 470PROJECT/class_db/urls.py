  
from django.urls import path, include
from class_db import views
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.user_login, name="login"),
    #path("signup", views.signup, name="signup"),
    #path("schedule", views.schedule, name="schedule"),
    path("information", views.insertRecordProf, name="information"),
    path("schedule", views.insertRecordProfPref, name="schedule"),
    path("about", views.about, name="about"),
    path("logout", views.logout, name="logout"),
    path("register", views.register_request, name="register")
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]