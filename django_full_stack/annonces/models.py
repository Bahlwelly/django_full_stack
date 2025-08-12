from django.db import models
from authentification.models import User

# Create your models here.
class Category (models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    

class Annonce (models.Model) :
    titre = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/annonces', null=True, blank=True)
    STATUS = [
        ('EN ATTENTE', 'En attente'),
        ('EN ATTENTE', 'Vlide'),
        ('REJETE', 'Rejete'),
    ]

    status = models.CharField(max_length=10, choices=STATUS, default='EN ATTENTE')

    