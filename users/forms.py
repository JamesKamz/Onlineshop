from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Profiles



class RegisterForm(UserCreationForm):
    username=forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        return user

  
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    contact = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'contact'] 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['cover_image', 'address', 'telephone']     