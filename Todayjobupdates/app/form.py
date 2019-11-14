
from .models import StudentModel,JobDetails
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"
        template_name="reg.html"
        widgets = {
            'password': forms.PasswordInput(),
        }

class JobDetailsForm(forms.ModelForm):
    class Meta:
        model=JobDetails
        fields="__all__"
        template_name= "Postjobs.html"