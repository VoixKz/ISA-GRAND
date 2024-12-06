from django.contrib import admin
from .models import CourseModel, VacancyModel

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(VacancyModel)