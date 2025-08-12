from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Annonce, Category

# Create your views here.
@login_required(login_url='login')

def home_view(request):
    categories = Category.objects.prefetch_related('annonce_set').all()
    return render(request, 'home.html', {'categories': categories})
