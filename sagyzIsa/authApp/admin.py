from django.contrib import admin
from .models import CustomUser, Employer, PersonalUser, Advisor

admin.site.register(CustomUser)
admin.site.register(Employer)
admin.site.register(PersonalUser)
admin.site.register(Advisor)