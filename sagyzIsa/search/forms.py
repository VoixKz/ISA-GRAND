from django import forms
from .models import VacancyModel, CourseModel

class VacancyForm(forms.ModelForm):
    class Meta:
        model = VacancyModel
        fields = [
            'vacancy_title', 'vacancy_description', 'vacancy_area', 
            'vacancy_requirements', 'vacancy_salary', 'vacancy_location', 
            'vacancy_company', 'is_hot'
        ]
        widgets = {
            'vacancy_title': forms.TextInput(attrs={'class': 'form-control'}),
            'vacancy_description': forms.Textarea(attrs={'class': 'form-control'}),
            'vacancy_area': forms.TextInput(attrs={'class': 'form-control'}),
            'vacancy_requirements': forms.Textarea(attrs={'class': 'form-control'}),
            'vacancy_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'vacancy_location': forms.TextInput(attrs={'class': 'form-control'}),
            'vacancy_company': forms.TextInput(attrs={'class': 'form-control'}),
            'is_hot': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = ['course_name', 'course_description', 'course_duration', 'course_area', 'course_price', 'course_author']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control'}),
            'course_duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_area': forms.TextInput(attrs={'class': 'form-control'}),
            'course_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_author': forms.TextInput(attrs={'class': 'form-control'}),
        }