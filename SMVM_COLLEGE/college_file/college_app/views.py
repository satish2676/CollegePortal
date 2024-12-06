from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # Check if user is staff/admin
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request,"Invalid credentials or not an admin.")
            return render(request, 'login.html',)
    return render(request, 'login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def student_login(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(student_id=student_id)
            if student.password == password:
                request.session['student_id'] = student.student_id  # Store the student ID in session
                return redirect('base')  # Redirect to base page after successful login
            else:
                messages.error(request, 'Invalid password')
        except Student.DoesNotExist:
            messages.error(request, 'Student not found')

    return render(request, 'login.html')



def base(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(student_id=student_id)
    return render(request, 'base.html', {'student': student})



from .models import Student
@login_required
def admin_dashboard(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'admin_dashboard.html', {'students': students})


# views.py
from django.shortcuts import get_object_or_404
from .forms import StudentForm

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})


# views.py
@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student.delete()
    return redirect('admin_dashboard')


def home(request):
    # Get the student based on the logged-in student or the session
    student_id = request.session.get('student_id')
    # If you're using session to store student ID
    if student_id:
        try:
            student = Student.objects.get(student_id=student_id)  # Assuming 'id' is the primary key for student
            return render(request, 'home.html', {'student': student})
        except Student.DoesNotExist:
            # Handle case where the student doesn't exist
            return render(request, 'home.html', {'error': 'Student not found'})
    else:
        return render(request, 'home.html', {'error': 'No student logged in'})

from .models import Marks
def marks(request):
    student_id = request.session.get('student_id')
    marks = Marks.objects.filter(student_id=student_id)
    student = Student.objects.get(student_id=student_id)  # Assuming you have a related marks model or field
    return render(request, 'marks.html', { 
        'marks': marks,
        'student': student
        })

from .models import Attendance
def attendance(request):
    student_id = request.session.get('student_id')  # Get student_id from session
    attendances = Attendance.objects.filter(student_id=student_id)
    student = Student.objects.get(student_id=student_id)  # Fetch attendance for the student
    return render(request, 'attendance.html', {
        'attendances': attendances,
        'student': student
        })



from .models import Backlogs

def backlogs(request):
    student_id = request.session.get('student_id')  # Get student_id from session
    backlogs = Backlogs.objects.filter(student_id=student_id)
    student = Student.objects.get(student_id=student_id)  # Fetch backlogs for the student
    return render(request, 'backlogs.html', {
        'backlogs': backlogs,
        'student': student
        })



from .models import Student

def personal_details(request):
    student_id = request.session.get('student_id')  # Get student_id from session
    student = Student.objects.get(student_id=student_id)  # Fetch personal details for the student
    return render(request, 'personal_details.html', {'student': student})


from .models import FeeDetails

def fee_details(request):
    student_id = request.session.get('student_id')  # Get student_id from session
    fee_details = FeeDetails.objects.filter(student_id=student_id)
    student = Student.objects.get(student_id=student_id)  # Fetch fee details for the student
    return render(request, 'fee_details.html', {
        'fee_details': fee_details,
        'student': student
        })


from .models import Complaints

def complaints(request):
    student_id = request.session.get('student_id')  # Get student_id from session
    complaints = Complaints.objects.filter(student_id=student_id)
    student = Student.objects.get(student_id=student_id)  # Fetch complaints made by the student
    return render(request, 'complaints.html', {
        'complaints': complaints,
        'student': student
        })



def logout(request):
    # Clear the session and redirect to the login page or home page
  # This clears the session completely
    return redirect('admin_login')  # Redirect to the login page