from .models import Job_detail,Applicant
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

        
class AddJobs(ModelForm):
    job_dateline = forms.DateField(widget=forms.SelectDateWidget(years=range(2024,2030)),required=False)

    class Meta:
        model = Job_detail

        exclude = ['user', 'job_published', 'status']

        widgets = {

            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name'
            }),

            'company_details': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Details'
            }),

            'job_post': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Post'
            }),

            'job_category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'job_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Location'
            }),

            'job_nature': forms.Select(attrs={
                'class': 'form-control'
            }),

            'job_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Salary'
            }),

            'job_desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job Description',
                'rows': 4
            }),

            'job_responsibility': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job Responsibility',
                'rows': 4
            }),

            'job_qualification': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job Qualification',
                'rows': 4
            }),

            'job_vacancy': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vacancy'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

        
class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
class JSignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name','email','website','cv','cover_letter']
        
class EmployerStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['applicant_status']

