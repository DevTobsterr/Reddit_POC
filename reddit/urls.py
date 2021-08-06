from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.application_home, name="application_home"),
    path('submission/results/', views.application_submission_results, name="application_submission_results"),
    path('submission/results/delete/<submission_id>', views.application_delete_submission, name="application_delete_submission"),

    path('submission/search/', views.application_submission_search, name="application_submission_search"),
    path('submission/search/query/', views.application_submission_query, name="application_submisson_search"),
    path('submission/esclations/', views.applcation_submission_esclation, name="application_submisson_esclation"),


]