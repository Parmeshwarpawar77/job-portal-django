from django.contrib import admin
from .models import Job_detail,Applicant
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=["company_name","company_details","job_post","job_location","job_nature","job_salary",
                  "job_published","job_dateline","job_desc","job_responsibility","job_qualification","job_vacancy"]
    
admin.site.register(Job_detail,JobAdmin)

class ApplicantAdmin(admin.ModelAdmin):
    list_display=["name","email","job","website","cv","cover_letter","applicant_status"]
    
admin.site.register(Applicant,ApplicantAdmin)