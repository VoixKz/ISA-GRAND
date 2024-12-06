from django.urls import path
from .views import cv_form, process_interest_form

urlpatterns = [
    path('cv_form/', cv_form, name='cv_form'),
    path('process_interest_form/', process_interest_form, name='process_interest_form'),
]