from django.db import models

class JobSeeker(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    skills = models.TextField()
    resume = models.FileField(upload_to="resumes/")

    def __str__(self):
        return self.fullname
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title
