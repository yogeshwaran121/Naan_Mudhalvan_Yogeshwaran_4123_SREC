from django import forms
from .models import user
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.ModelForm):
   password = forms.CharField(widget = forms.PasswordInput)
   confirm_password = forms.CharField(widget = forms.PasswordInput)

   class Meta:
      model = user
      fields = ['first_name' , 'last_name' , 'email' , 'password']

   def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get("password")
      confirm_password = cleaned_data.get("confirm_password")
      if password != confirm_password:
         raise forms.ValidationError("passwords do not match")
      
class LoginForm(AuthenticationForm):
   pass