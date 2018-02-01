from django import forms
from django.contrib.auth.models import User   #使用系统默认的用户模型
from .models import UserProfile, UserInfo

class LoginForm(forms.Form): #Forms是只对数据进行等级而不更改
    username = forms.CharField();
    password = forms.CharField(widget=forms.PasswordInput);

class RegistrationForm(forms.ModelForm):#Forms是只对数据进行等级并更改
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)

    class Meta:#确定所用的用户的数据模型
        model = User
        fields = ("username", "email")#确定所使用的用户模型中的部分属性

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
