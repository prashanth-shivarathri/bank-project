from django import forms
from . models import Bank


class Bankform(forms.ModelForm):
     class Meta:
          model=Bank
          fields=['name','account','phone','email','aadhar','dob','photo','gender']

