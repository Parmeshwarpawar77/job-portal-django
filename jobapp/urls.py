from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category/',views.category,name='category'),
    path('contact/',views.contact,name='contact'),
    path('login_employer/',views.login_employer,name='login_employer'),
    path('employer_signup/',views.employer_signup,name='employer_signup'),
    path('logout/',views.logout_user,name='logout'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('choose/', views.choose, name='choose'),
    #Employer
    path('employer/',views.employer,name='employer'),
    path('joblisting/',views.joblisting,name='joblisting'),
    path('addjobs/',views.addjobs,name='addjobs'),
    path('edit/<int:job_id>',views.edit,name='edit'),
    path('delete/<int:job_id>',views.delete,name='delete'),
    path('display',views.display,name='display'),
    path('view/<int:job_id>',views.view_applyer,name="view_applyer"),
    path('update_applicant_status/<int:applicant_id>/', views.update_applicant_status, name='update_applicant_status'),
    #job_seeker
    path('jobdetails/<int:job_id>/',views.jobdetails,name='jobdetails'),
    path('joblist/',views.joblist,name='joblist'),
    path('job_seeker_signup/',views.job_seeker_signup,name='job_seeker_signup'),
    path('login_job_seeker/',views.login_job_seeker,name='login_job_seeker'),
    path('applied_job/',views.applied_job,name='applied_job'),
    path('delete_applied/<int:app_id>',views.delete_applied,name='delete_applied'),
    path('search/', views.search_jobs, name='search_jobs'),
    path('404/', views.custom_404,name='custom_404'),
    
]