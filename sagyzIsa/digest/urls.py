from django.urls import path
from .views import get_digest, call_newsogus, call_egovus, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('get_digest/', get_digest, name="get_digest"),
    path('call_newsogus/', call_newsogus, name="call_newsogus"),
    path('call_egovus/', call_egovus, name="call_egovus"),
]