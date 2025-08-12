from django.db import models
from django.contrib.auth.models import AbstractUser # type: ignore

class User (AbstractUser) :
    telephone = models.CharField(max_length=8) 

    ROLE_CHOICES = [
        ('CLIENT', 'Client'),
        ('ADMIN', 'Admin')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CLIENT')

    def __str__(self):
        return f'{self.username}-{self.role}'
    
    