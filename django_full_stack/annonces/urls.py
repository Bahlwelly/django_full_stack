from django.urls import path
from .views import *
from authentification.views import login


urlpatterns = [
    path('/home/', home_view, name='home'),
    path('annonce/<int:pk>/', details_annonce_view, name='details_annonce'),
    path('annonces/privees/', annonces_privees, name='annonces_privees'),
    path('en/attente/', annonce_en_attente, name='annonces_en_attente'),
    path('valides/', annonces_valides, name='annonces_valides'),
    path('rejetes/', annonce_rejetes, name='annonces_rejetes'),
    path('ajouter/', ajouter_annonce, name='ajouter_annonce'),
    path('modifier/<int:pk>/', modifier_annonce, name='modifier_annonce'),
    path('supprimer/<int:pk>/', supprimer_annonce, name='supprimer_annonce'),
    path('modifier/<int:pk>/status/<str:new_status>', modifier_status, name='modifier_status'),
    path('ajouter/category/', ajouter_category, name='ajouter_category'),
    path('redirected/login/', login, name='login'),
]