from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100, primary_key=True) 
    password = models.CharField(max_length=50, )

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    # Add other personal details
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    department = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    emergency_contact = models.BigIntegerField()

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    marks_obtained_1st = models.IntegerField()
    marks_obtained_2nd = models.IntegerField()
    marks_obtained_3rd = models.IntegerField()
    marks_obtained_4th = models.IntegerField()
    marks_obtained_5th = models.IntegerField()
    marks_obtained_6th = models.IntegerField()
    total_marks_obtained = models.IntegerField()
    CGPA_1st = models.FloatField()
    CGPA_2nd = models.FloatField()
    CGPA_3rd = models.FloatField()
    CGPA_4th = models.FloatField()
    CGPA_5th = models.FloatField()
    CGPA_6th = models.FloatField()
    CGPA_total = models.FloatField()


class Backlogs(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    semester_1st = models.IntegerField(default=0)
    semester_2nd = models.IntegerField(default=0)
    semester_3rd = models.IntegerField(default=0)
    semester_4th = models.IntegerField(default=0)
    semester_5th = models.IntegerField(default=0)
    semester_6th = models.IntegerField(default=0)
    subject_code1 = models.IntegerField(default=0)
    subject_code2 = models.IntegerField(default=0)
    subject_code3 = models.IntegerField(default=0)
    subject_code4 = models.IntegerField(default=0)
    subject_code5 = models.IntegerField(default=0)
    subject_code6 = models.IntegerField(default=0)
    subject_name1 = models.CharField(max_length=100)
    subject_name2 = models.CharField(max_length=100)
    subject_name3 = models.CharField(max_length=100)
    subject_name4 = models.CharField(max_length=100)
    subject_name5 = models.CharField(max_length=100)
    subject_name6 = models.CharField(max_length=100)
    status1 = models.BooleanField(default=False)
    status2 = models.BooleanField(default=False)
    status3 = models.BooleanField(default=False)
    status4 = models.BooleanField(default=False)
    status5 = models.BooleanField(default=False)
    status6 = models.BooleanField(default=False)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    no_of_workingdays1 = models.IntegerField()
    no_of_workingdays2 = models.IntegerField()
    no_of_workingdays3 = models.IntegerField()
    no_of_workingdays4 = models.IntegerField()
    no_of_workingdays5 = models.IntegerField()
    no_of_workingdays6 = models.IntegerField()
    no_of_workingdays7 = models.IntegerField()
    no_of_workingdays8 = models.IntegerField()
    no_of_workingdays9 = models.IntegerField()
    no_of_workingdays10 = models.IntegerField()
    no_of_workingdays11 = models.IntegerField()
    no_of_workingdays12 = models.IntegerField()
    total_workingdays = models.IntegerField()
    no_of_days_present1 = models.IntegerField()
    no_of_days_present2 = models.IntegerField()
    no_of_days_present3 = models.IntegerField()
    no_of_days_present4 = models.IntegerField()
    no_of_days_present5 = models.IntegerField()
    no_of_days_present6 = models.IntegerField()
    no_of_days_present7 = models.IntegerField()
    no_of_days_present8 = models.IntegerField()
    no_of_days_present9 = models.IntegerField()
    no_of_days_present10 = models.IntegerField()
    no_of_days_present11 = models.IntegerField()
    no_of_days_present12 = models.IntegerField()
    total_days_present = models.IntegerField()
    percentage1 = models.FloatField()
    percentage2 = models.FloatField()
    percentage3 = models.FloatField()
    percentage4 = models.FloatField()
    percentage5 = models.FloatField()
    percentage6 = models.FloatField()
    percentage7 = models.FloatField()
    percentage8 = models.FloatField()
    percentage9 = models.FloatField()
    percentage10 = models.FloatField()
    percentage11 = models.FloatField()
    percentage12 = models.FloatField()
    total_percentage = models.FloatField()


class FeeDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    total_fee = models.IntegerField()
    amount_paid = models.IntegerField()
    remaining_fee = models.IntegerField()
    due_date = models.DateField(auto_now_add=True)
    status1 = models.BooleanField(default=True)
    status2 = models.BooleanField(default=True)
    status3 = models.BooleanField(default=True)
    status4 = models.BooleanField(default=True)
    status5 = models.BooleanField(default=True)
    status6 = models.BooleanField(default=True)


class Complaints(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    complaint_text = models.TextField()
    complaint_date = models.DateField(auto_now_add=True)


class Home(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    img = models.ImageField(upload_to='images/')
