from django import forms
from .models import User

class LoginForm(forms.Form):

    email = forms.CharField(max_length= 200, widget=(forms.EmailInput()))
    password = forms.CharField(max_length= 200, widget=(forms.PasswordInput()))

    def __init__(self, *args, **kwargs):
        count = 0
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            count += 1
            field.field.widget.attrs['class'] = f'form-field-{count} login-form-field'
            field.field.widget.attrs['id'] = f'form-field-{count}'


class RegisterForm(forms.Form):


    email = forms.CharField(max_length= 200, widget=(forms.EmailInput()))
    FirstName = forms.CharField(max_length= 15)
    LastName = forms.CharField(max_length= 15)
    password = forms.CharField(max_length= 80, widget=(forms.PasswordInput()))
    password_repeat = forms.CharField(max_length= 200, widget=(forms.PasswordInput()))

    def __init__(self, *args, **kwargs):

        count = 0
        Values = ['email', 'FirstName', 'LastName', 'password', 'password_repeat']
        
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            count += 1
            field.field.widget.attrs['class'] = f'form-field-{count} register-form-field'
            field.field.widget.attrs['id'] = f'form-field-{count}'
            field.field.widget.attrs['name'] = f'{Values[count - 1]}'
