from django.db import models
from django.contrib.auth.models import User

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Remote/WFH','Remote/WFH'),
    )

CATEGORY_CHOICES = [
    ('marketing', 'Marketing'),
    ('customer_service', 'Customer Service'),
    ('human_resource', 'Human Resource'),
    ('information technology', 'Information Technology'),
    ('business_development', 'Business Development'),
    ('sales_communication', 'Sales & Communication'),
    ('teaching_education', 'Teaching & Education'),
]

Status_type=(
    ('Active','Active'),
    ('Not Active','Not Active'),
)

class Job_detail(models.Model):
    company_name = models.CharField(max_length=50)
    company_details = models.CharField(max_length=100)
    job_post = models.CharField(max_length=70)
    job_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    job_location = models.CharField(max_length=50)
    job_nature = models.CharField(max_length=15 , choices=JOB_TYPE)
    job_salary = models.IntegerField(default=1)
    job_published = models.DateTimeField(auto_now=True)
    job_dateline = models.DateField()
    job_desc = models.CharField(max_length=250)
    job_responsibility = models.CharField(max_length=400)
    job_qualification = models.CharField(max_length=400)
    job_vacancy = models.IntegerField(default=1)
    status = models.CharField(max_length=15,choices=Status_type,default='Active')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]    
class Applicant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=1000)
    job = models.ForeignKey(Job_detail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applicant_status =models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()