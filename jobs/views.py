from .models import JobSeeker
from django.shortcuts import render, redirect
from .models import Job,Application

def home(request):
    
    query = request.GET.get("search")
    location = request.GET.get("location")

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)

    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, "home.html", {
        "jobs": jobs
    })

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = JobSeeker.objects.get(email=email, password=password)
            return redirect("home")
        except JobSeeker.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid Email or Password"})

    return render(request, "login.html")

def register(request):
    
    if request.method == "POST":

        JobSeeker.objects.create(

            fullname=request.POST["fullname"],
            email=request.POST["email"],
            password=request.POST["password"],
            phone=request.POST["phone"],
            dob=request.POST["dob"],
            city=request.POST["city"],
            qualification=request.POST["qualification"],
            skills=request.POST["skills"],
            resume=request.FILES["resume"]

        )

        return redirect("login")

    return render(request, "register.html")

def apply_job(request, job_id):
    
    job = Job.objects.get(id=job_id)

    jobseeker = JobSeeker.objects.first()

    Application.objects.create(
        job=job,
        jobseeker=jobseeker
    )

    return redirect("home")

def my_applications(request):
    
    jobseeker = JobSeeker.objects.first()

    applications = Application.objects.filter(jobseeker=jobseeker)

    return render(request, "my_applications.html", {
        "applications": applications
    })
    
def add_job(request):
    
    if request.method == "POST":

        Job.objects.create(
            title=request.POST["title"],
            company=request.POST["company"],
            location=request.POST["location"],
            salary=request.POST["salary"],
            description=request.POST["description"]
        )

        return redirect("home")

    return render(request, "add_job.html")

def profile(request):
    
    user = JobSeeker.objects.first()

    return render(request, "profile.html", {
        "user": user
    })
    
def edit_profile(request):
    
    user = JobSeeker.objects.first()

    if request.method == "POST":

        user.fullname = request.POST["fullname"]
        user.phone = request.POST["phone"]
        user.city = request.POST["city"]
        user.qualification = request.POST["qualification"]
        user.skills = request.POST["skills"]

        if "resume" in request.FILES:
            user.resume = request.FILES["resume"]

        user.save()

        return redirect("profile")

    return render(request, "edit_profile.html", {
        "user": user
    })


def dashboard(request):

    total_jobs = Job.objects.count()
    total_jobseekers = JobSeeker.objects.count()
    total_applications = Application.objects.count()

    jobs = Job.objects.all()[:5]

    return render(request, "dashboard.html", {
        "total_jobs": total_jobs,
        "total_jobseekers": total_jobseekers,
        "total_applications": total_applications,
        "jobs": jobs,
    })    
    