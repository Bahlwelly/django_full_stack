from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm

class loginForm (forms.Form) :
    password = forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField()
    # class Meta :
    #     model = User
    #     fields = ['username', 'password']
    #     help_texts = {
    #         'username' : '',
    #     }


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password :  
            try : 
                user = User.objects.get(username = username)
                if not check_password(password, user.password) :
                    raise forms.ValidationError("Nom ou mot de pass invalides")
            
            except User.DoesNotExist :
                raise forms.ValidationError("Nom ou mot de pass invalides")
        
        return cleaned_data 
    

class registerForm (UserCreationForm) : 
    
    ROLE_CHOICES = [
        ('CLIENT', 'Client'),
        ('ADMIN', 'Admin')
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label='Selectioner votre role')
    class Meta :
        model = User
        fields = ['username', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in ['username', 'password1', 'password2'] :
            self.fields[f].help_text = ''