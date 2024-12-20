from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','name' ,'password1', 'password2', 'bio', 'description']