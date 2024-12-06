from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import VacancyModel, CourseModel
from authApp.models import Employer
from .forms import VacancyForm, CourseForm


def courses_view(request):
    search_query = request.GET.get('search', '').lower()
    selected_area = request.GET.get('area', '').lower()
    sort_order = request.GET.get('sort', '')

    courses = CourseModel.objects.all()

    if search_query:
        courses = courses.filter(course_name__icontains=search_query)

    if selected_area:
        courses = courses.filter(course_area__icontains=selected_area)

    if sort_order == 'duration':
        courses = courses.order_by('course_duration')
    elif sort_order == 'price':
        courses = courses.order_by('course_price')

    areas = CourseModel.objects.values_list('course_area', flat=True).distinct()
    context = {
        'courses': courses,
        'areas': areas,
    }
    return render(request, 'search/search_courses.html', context)


def vacancies_view(request):
    search_query = request.GET.get('search', '').lower()
    selected_specialty = request.GET.get('specialty', '').lower()
    sort_order = request.GET.get('sort', '')

    vacancies = VacancyModel.objects.all()
    hot_vacancies = vacancies.filter(is_hot=True)

    if search_query:
        vacancies = vacancies.filter(vacancy_title__icontains=search_query)

    if selected_specialty:
        vacancies = vacancies.filter(vacancy_area__icontains=selected_specialty)

    if sort_order == 'date':
        vacancies = vacancies.order_by('created_at')
    elif sort_order == 'salary':
        vacancies = vacancies.order_by('vacancy_salary')

    specialties = VacancyModel.objects.values_list('vacancy_area', flat=True).distinct()
    context = {
        'vacancies': vacancies,
        'hot_vacancies': hot_vacancies,
        'specialties': specialties,
    }
    return render(request, 'search/search_vacancies.html', context)


@login_required
def add_course_view(request):
    if not hasattr(request.user, 'employer'):
        return redirect('home')
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'search/add_course.html', {'form': form})


@login_required
def add_vacancy_view(request):
    if not hasattr(request.user, 'employer'):
        return redirect('home')

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancies')
    else:
        form = VacancyForm()
    return render(request, 'search/add_vacancy.html', {'form': form})


def course_detail_view(request, id):
    course = get_object_or_404(CourseModel, id=id)
    return render(request, 'search/course_detail.html', {'course': course})

def vacancy_detail_view(request, id):
    vacancy = get_object_or_404(VacancyModel, id=id)
    return render(request, 'search/vacancy_detail.html', {'vacancy': vacancy})