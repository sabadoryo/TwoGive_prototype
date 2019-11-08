from django.contrib.auth.models import User
from django.forms import ModelForm

from TwoGive.models import authUser


class RenterSignUpForm(ModelForm):
    class Meta:
        model = authUser
        fields = ('username', 'iin', 'num_tel', 'email', 'password')


class UserLogInForm(ModelForm):
    class Meta:
        model = authUser
        fields = ('username', 'password')
