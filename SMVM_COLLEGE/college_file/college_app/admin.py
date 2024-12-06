
from django.contrib import admin
from .models import Student, Marks, Attendance, Backlogs, FeeDetails, Complaints,Home

admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Backlogs)
admin.site.register(FeeDetails)
admin.site.register(Complaints)
admin.site.register(Attendance)
admin.site.register(Home)
