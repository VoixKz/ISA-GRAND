from django.urls import path
from .views import signup_view, login_view, logout_view, select_personality_view, dashboard_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('select_personality/', select_personality_view, name='select_personality'),
    path('dashboard/', dashboard_view, name='dashboard'),
]