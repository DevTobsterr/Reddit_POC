from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.application_home, name="application_home"),
    path('submission/', views.application_submisson_search, name="application_submisson_search"),
    path('submission/results', views.application_submisson_results, name="application_submisson_results"),

    


]