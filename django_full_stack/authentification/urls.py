from django.urls import path
from .views import *
from annonces.views import home_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),
]
