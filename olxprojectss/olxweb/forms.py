from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import Userprofile,Products,Questions

class Registrationform(UserCreationForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"})
            }
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserprofileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=["profile_pic","address","place","contact_number"]

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=["product_name","description","image","price","category"]



class questionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=["description"]