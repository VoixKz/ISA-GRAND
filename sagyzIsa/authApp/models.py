from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator, EmailValidator
from datetime import date


CITY_CHOICES = [
    ('almaty', 'Алматы'),
    ('nur-sultan', 'Нур-Султан'),
    ('shymkent', 'Шымкент'),
    ('karaganda', 'Караганда'),
    ('aktobe', 'Актобе'),
    ('taraz', 'Тараз'),
    ('pavlodar', 'Павлодар'),
    ('uralsk', 'Уральск'),
    ('ust-kamenogorsk', 'Усть-Каменогорск'),
    ('semey', 'Семей'),
    ('aktau', 'Актау'),
    ('atyrau', 'Атырау'),
    ('kostanay', 'Костанай'),
    ('kokshetau', 'Кокшетау'),
    ('petropavl', 'Петропавловск'),
    ('kyzylorda', 'Кызылорда'),
]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address.")])
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default='astana')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=255)
    is_educational_institution = models.BooleanField(default=False)
    bin_number = models.CharField(max_length=12)
    industry = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])


class PersonalUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(validators=[MinValueValidator(limit_value=date(1900, 1, 1), message="Enter a valid birth date.")])
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    education = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)


class Advisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])