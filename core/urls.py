from django.urls import path
from .views import homepage
from .views import profile

urlpatterns = [
    path('', homepage, name='homepage'),
    path('profile/', profile, name='profile'),
]