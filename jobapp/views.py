from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Applicant,Job_detail,Contact
from .forms import AddJobs,SignupForm,JSignupForm,JobApplicationForm,EmployerStatusUpdateForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def category(request):
    return render(request,'category.html')

def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Message Sent Successfully")

        return redirect('contact')

    return render(request, 'contact.html')

def jobdetails(request,job_id):
    job = Job_detail.objects.get(pk = job_id)
    if request.user.is_authenticated:
        has_applied = Applicant.objects.filter(user=request.user, job=job).exists()
    # if job.status != 'Active':
    #     messages.error(request, "This job is not currently open for applications.")
    #     return redirect('joblist') 
        
    if request.user.is_authenticated:
        if has_applied:
            messages.success(request,"Already applied")
            return render(request, 'job-detail.html', {'jobs': job,'has_applied':has_applied})
    if request.method == 'POST':
        form = JobApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.job = job
            f.user = request.user
            f.save()
            print(f.save)
            messages.success(request,"Job Applied")
            return redirect('applied_job')
        else:
            print(form.errors)
            messages.error(request,"Error! Incorrect Input!!")
    else:
        form = JobApplicationForm()
    return render(request,'job-detail.html', {'form': form,'jobs':job})


def joblist(request):
    jobs1 = Job_detail.objects.filter(job_nature = 'Full Time')
    jobs2 = Job_detail.objects.filter(job_nature = 'Part Time')
    jobs3 = Job_detail.objects.filter(job_nature = 'Remote/WFH')
    
    return render(request,'job-list.html',{'jobs1':jobs1,'jobs2':jobs2,'jobs3':jobs3})

#employer_signup & login
def employer_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('login_employer')
        else:
            print(form.errors)
            return render(request, 'employer_signup.html', {'form': form})
    else: 
        form = SignupForm()
        return render(request, 'employer_signup.html', {'form': form})
    
def login_employer(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,("Logged in Successfully"))
            return redirect('employer')
        else:
            messages.error(request,"Error! Incorrect Input!!")
            return redirect('login_employer')
    return render(request,"login-employer.html")

#job_seeker_signup & login
def job_seeker_signup(request):
    if request.method == 'POST':
        form = JSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('login_job_seeker')
        else:
            print(form.errors)
            return render(request, 'employer_signup.html', {'form': form})
    else:
        form = JSignupForm()
        return render(request, 'job_seeker_signup.html', {'form': form})


def login_job_seeker(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,("Logged in Successfully"))
            return redirect('/')
        else:
            messages.error(request,"Error! Incorrect Input!!")
            return redirect('login_job_seeker')
    return render(request,"login-job_seeker.html")

#logout
def logout_user(request):
    logout(request)
    messages.success(request,("You are Logout"))
    return redirect("/")

def applied_job(request):
    applied = Applicant.objects.filter(user=request.user)
    return render(request, 'applied-job.html', {'applied': applied})

def testimonial(request):
    return render(request,'testimonial.html')

#employer views

def joblisting(request,):
    jobs = Job_detail.objects.all()
    return render(request,'joblisting.html',{'jobs':jobs})

def choose(request):
    return render(request, 'choose.html')

def employer(request):
    return render(request,'employer.html')

def addjobs(req):
    if req.user.is_authenticated:
        if req.method == "GET":
            form = AddJobs()
            return render(req,"addjobs.html",{'form':form})
        else:
            form = AddJobs(req.POST)
            if form.is_valid():
                f=form.save(commit=False)
                f.user=req.user
                f.save()
                messages.success(req,("Job Added Successfully"))
                return redirect("employer")
            else:
                messages.error(req,"incorrect data")
                return render(req,"addjobs.html",{'form':form})
    else:
        return redirect('/login_employer')
    
def display(req):
    jobs = Job_detail.objects.filter(user=req.user)
    context = {'jobs':jobs}
    return render(req,"display.html",context) 
    
def edit(req,job_id):
    job= Job_detail.objects.get(pk=job_id)
    if req.method == 'POST':
        form = AddJobs(req.POST,instance=job)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=req.user
            f.save()
        return redirect ("employer")
    else:
        form = AddJobs(instance=job)
        return render(req,"editjob.html",{'form':form})
    
def delete(req,job_id):
    print("ID to be deleted",job_id)
    m = Job_detail.objects.filter(pk=job_id)
    m.delete()
    return redirect('display')

def delete_applied(req,app_id):
    a=Applicant.objects.filter(pk=app_id)
    a.delete()
    return redirect('applied_job')


def view_applyer(req,job_id):
    job=Job_detail.objects.get(pk=job_id)
    view = Applicant.objects.filter(job=job)
    return render(req,"view_applyer.html",{'job':job,'view':view})

def update_applicant_status(request, applicant_id):
    applicant = Applicant.objects.get(id=applicant_id)
    
    if request.method == 'POST':
        form = EmployerStatusUpdateForm(request.POST,instance=applicant)
        if form.is_valid():
            old_status = applicant.applicant_status
            form.save()
            new_status = applicant.applicant_status
            if old_status != new_status and new_status in ['Approved', 'Rejected']:
                return HttpResponse("Status Updated")
            subject = ''
            message = ''
            if applicant.applicant_status == 'Approved':
                subject = 'Congratulations! Your Application has been Accepted'
                message = f'Dear {applicant.name},\n\nCongratulations! Your application has been accepted.\n\nBest regards,\nYour Organization'
                print(new_status)
            elif applicant.applicant_status == 'Rejected':
                subject = 'Regarding Your Job Application'
                message = f'Dear {applicant.name},\n\nWe regret to inform you that your application has been rejected.\n\nBest regards,\nYour Organization'
            
            if subject and message:
                from_email = 'pawar.parm77@gmail.com'
                to_email = applicant.email
                send_mail(subject, message, from_email, [to_email])
                print('done')
                return HttpResponse("Notification email sent successfully")
    else:
        form = EmployerStatusUpdateForm(instance=applicant)
    
    return render(request, 'view_applyer.html', {'form': form,'applicant':applicant})

def search_jobs(request):
    keyword = request.GET.get('keyword')
    location = request.GET.get('location')
    category = request.GET.get('category')

    jobs = Job_detail.objects.all()

    if keyword:
        jobs = jobs.filter(job_post__icontains=keyword)
    if location:
        jobs = jobs.filter(job_location__icontains=location)
    if category:
        jobs = jobs.filter(job_category__icontains=category)

    return render(request, 'search_results.html', {'jobs': jobs})
def custom_404(request):
    return render(request, '404.html')
