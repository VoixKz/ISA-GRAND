from django.urls import path
from .views import vacancies_view, courses_view, add_course_view, add_vacancy_view, course_detail_view, vacancy_detail_view

urlpatterns = [
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/<int:id>/', vacancy_detail_view, name='vacancy'),
    path('courses/', courses_view, name='courses'),
    path('courses/<int:id>/', course_detail_view, name='course'),
    path('add_course/', add_course_view, name='add_course'),
    path('add_vacancy/', add_vacancy_view, name='add_vacancy'),
]