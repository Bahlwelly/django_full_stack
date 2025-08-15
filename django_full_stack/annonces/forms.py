from django import forms
from .models import Annonce , Category

class Annonce_form (forms.ModelForm) :
    class Meta :
        model = Annonce
        fields = ['titre', 'description', 'prix', 'category', 'status', 'image']


class Category_form (forms.ModelForm) :
    class Meta :
        model = Category
        fields = ['name']