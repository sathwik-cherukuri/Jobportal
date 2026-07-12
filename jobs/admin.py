from django.contrib import admin
from .models import JobSeeker, Job,Application

admin.site.register(JobSeeker)
admin.site.register(Job)
admin.site.register(Application)
