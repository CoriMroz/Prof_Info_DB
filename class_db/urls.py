from django.urls import path
from class_db import views
from . import views

app_name = 'scheduling'
urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    #path("signup", views.signup, name="signup"),
    #path("schedule", views.schedule, name="schedule"),
    path("signup", views.insertRecordProf, name="signup"),
    path("schedule", views.insertRecordProfPref, name="schedule")
]