from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, EmailField, Form
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class RegisterForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', )

    def clean_password(self):
        return make_password(self.cleaned_data['password'])

class CustomLoginForm(Form):
    username  = CharField(max_length=200)
    firs_name = CharField(max_length=200)
    password = CharField()


    def clean_password(self):
        return make_password(self.cleaned_data['password'])