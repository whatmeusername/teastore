from django import forms
from .models import User

class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length= 200, widget=(forms.PasswordInput(attrs={'class': 'PasswordField', 'id': 'PasswordField'})))
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        count = 0
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            count += 1
            field.field.widget.attrs['class'] = f'form-field-{count}'
            field.field.widget.attrs['id'] = f'form-field-{count}'
