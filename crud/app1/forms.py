from django import forms
from django.shortcuts import render
from .models import addstudent

class addstud(forms.ModelForm):
    class Meta: 
        model = addstudent
        fields ='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'email':forms.EmailInput(attrs={'class':'form-control mb-3'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control mb-3'}),
            #render_value=True to display password when edit button is clicked
        }