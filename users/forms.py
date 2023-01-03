from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm , SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm): #This will go ahead and generate field for every editable field.
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)



        
