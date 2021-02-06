from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username =forms.CharField(label='Email or username',max_length=20,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'your email or username'}))
    password=forms.CharField(max_length=25,widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'your password'}))


class UserRegisterForm(forms.Form):
    username =forms.CharField(max_length=20,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'your password'}))
    password1=forms.CharField(label='password',max_length=25,widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'your password'}))
    password2=forms.CharField(label='passwordConfig',max_length=25,widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'your password'}))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'your Email'}))

    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('this is email ago exists')
        return email
    # def class_password2(self):
    #     p1=self.cleaned_data['password1']
    #     p2=self.cleaned_data['password2']
    #     if p1 != p2 :
    #         raise forms.ValidationError('password not Congig')
    #     return p1

    def clean(self):
        cleaned_data=super().clean()
        p1=cleaned_data.get('password1')
        p2=cleaned_data.get('password2')
        if p1 and p2:
            if p1 != p2 :
                raise forms.ValidationError('password not Config')

        
