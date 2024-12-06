from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, RegexValidator, EmailValidator
from django.utils import timezone



class CourseModel(models.Model):
    course_name = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Название курса"
    )
    course_description = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(1000)],
        verbose_name="Описание курса"
    )
    course_duration = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(365)],
        verbose_name="Длительность курса"
    )
    course_area = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Область курса",
    )
    course_price = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100000.0)],
        verbose_name="Цена курса"
    )
    course_author = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Автор курса",        
    )

    def __str__(self):
        return self.course_name
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"



class VacancyModel(models.Model):
    vacancy_title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Название вакансии"
    )
    vacancy_description = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(1000)],
        verbose_name="Описание вакансии"
    )
    vacancy_area = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Область вакансии"
    )
    vacancy_requirements = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(1000)],
        verbose_name="Требования к вакансии"
    )
    vacancy_salary = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1000000.0)],
        verbose_name="Зарплата"
    )
    vacancy_location = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Местоположение вакансии"
    )
    vacancy_company = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        verbose_name="Компания"
    )
    is_hot = models.BooleanField(
        default=False,
        verbose_name="Горячая вакансия"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.vacancy_title

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"