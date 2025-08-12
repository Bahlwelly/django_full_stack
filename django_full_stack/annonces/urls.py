from django.urls import path
from .views import *
from authentification.views import login


urlpatterns = [
    path('/home/', home_view, name='home'),
    path('redirected/login/', login, name='login'),
]