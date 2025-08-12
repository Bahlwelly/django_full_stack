from django.contrib import admin
from annonces.models import Annonce, Category

# Register your models here.
admin.site.register(Annonce)
admin.site.register(Category)