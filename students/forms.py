from django import forms
from .models import students

class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['name', 'email', 'phone_no']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
        }
