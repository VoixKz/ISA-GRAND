from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Employer, PersonalUser, Advisor

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'city')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }

class EmployerSignUpForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'is_educational_institution', 'bin_number', 'industry', 'phone_number')
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_educational_institution': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bin_number': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PersonalSignUpForm(forms.ModelForm):
    class Meta:
        model = PersonalUser
        fields = ('full_name', 'birth_date', 'phone_number', 'education', 'experience')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),

        }

class AdvisorSignUpForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = ('name', 'workplace', 'phone_number')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'workplace': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))