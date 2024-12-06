from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, EmployerSignUpForm, PersonalSignUpForm, AdvisorSignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Employer, PersonalUser, Advisor





def select_personality_view(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        if account_type:
            request.session['account_type'] = account_type
            return redirect('signup')
    return render(request, 'authApp/select_personality.html', )


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'authApp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    account_type = request.session.get('account_type', 'personal')
    if account_type == 'employer':
        user_form_class = CustomUserCreationForm
        profile_form_class = EmployerSignUpForm
    elif account_type == 'personal':
        user_form_class = CustomUserCreationForm
        profile_form_class = PersonalSignUpForm
    elif account_type == 'advisor_edu' or account_type == 'advisor_non_edu':
        user_form_class = CustomUserCreationForm
        profile_form_class = AdvisorSignUpForm
    else:
        user_form_class = CustomUserCreationForm
        profile_form_class = PersonalSignUpForm

    if request.method == 'POST':
        user_form = user_form_class(request.POST)
        profile_form = profile_form_class(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = user_form_class()
        profile_form = profile_form_class()

    return render(request, 'authApp/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'account_type': account_type})


@login_required
def dashboard_view(request):
    custom_user = CustomUser.objects.get(email=request.user.email)
    
    # Получение связанных данных
    user_data = {
        'custom_user': custom_user,
    }

    try:
        user_data['personal_user'] = custom_user.personaluser
    except PersonalUser.DoesNotExist:
        user_data['personal_user'] = None

    try:
        user_data['employer'] = custom_user.employer
    except Employer.DoesNotExist:
        user_data['employer'] = None

    try:
        user_data['advisor'] = custom_user.advisor
    except Advisor.DoesNotExist:
        user_data['advisor'] = None

    return render(request, 'authApp/dashboard.html', user_data)