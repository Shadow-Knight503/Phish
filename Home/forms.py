from django import forms
from .models import UserCreds


class UserForm(forms.ModelForm):
    class Meta:
        model = UserCreds
        fields = ['UserName', 'PassWord']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['UserName'].widget.attrs['class'] = 'Fld browser-default'
        self.fields['UserName'].widget.attrs['placeholder'] = 'Username'
        self.fields['PassWord'].widget.attrs['class'] = 'Fld browser-default'
        self.fields['PassWord'].widget.attrs['placeholder'] = 'Password'
        self.fields['PassWord'].widget.attrs['type'] = 'password'

