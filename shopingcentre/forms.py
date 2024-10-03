from django.forms import ModelForm
from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'placeholder':'Enter Your Password',
            'class':'form-row',
            'type':'text'
        })
        self.fields["password2"].widget.attrs.update({
            'name':'password2',
            'id':'password2',
            'placeholder':'Confirm Your Password',
            'class':'form-row',
            'type':'text'
        })
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'placeholder':'Enter Username',
            'class':'form-row',
            'type':'text'
        })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'id':'email',
            'placeholder':'Enter Your Email',
            'class':'form-row',
            'type':'email'
        })
        self.fields["first_name"].widget.attrs.update({
            'name':'firstname',
            'id':'firstname',
            'placeholder':'Enter Your First Name',
            'class':'form-row',
            'type':'text'
        })
        self.fields["last_name"].widget.attrs.update({
            'name':'lastname',
            'id':'lastname',
            'placeholder':'Enter Your Last Name',
            'class':'form-row',
            'type':'text'
        })
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']