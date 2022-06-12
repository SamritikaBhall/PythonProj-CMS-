from django.db import models


# Create your models here.
class Student(models.Model):
    Stu_gender = [('M', 'Male'), ('F', 'Female')]
    # Stu_id = models.IntegerField()
    Stu_Fname = models.CharField(max_length=100)
    Stu_Lname = models.CharField(max_length=100)
    Stu_email = models.CharField(max_length=100)
    Stu_Pass = models.CharField(max_length=100)
    Stu_dob = models.DateTimeField()
    Stu_grade = models.CharField(max_length=3)
    Stu_marks = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Stu_gender)

    def __str__(self):
        return self.Stu_Fname


class Staff(models.Model):
    Stf_gender = [('M', 'Male'), ('F', 'Female')]
    # Stf_id = models.IntegerField()
    Stf_Fname = models.CharField(max_length=100)
    Stf_Lname = models.CharField(max_length=100)
    Stf_email = models.CharField(max_length=100)
    Stf_Pass = models.CharField(max_length=100)
    Stf_dob = models.DateTimeField()
    Stf_Exp = models.IntegerField()
    Sub_Code = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Stf_gender)

    def __str__(self):
        return self.Stf_id


class Course(models.Model):
    # Crs_Code = models.IntegerField()
    Crs_Name = models.CharField(max_length=100)
    Sub_Code = models.IntegerField()
    Crs_Initials = models.CharField(max_length=2)
    Crs_Credit = models.IntegerField()

    def __str__(self):
        return self.Crs_Code


class Subjects(models.Model):
    # Sub_Code = models.IntegerField()
    Sub_Name = models.CharField(max_length=100)
    Crs_Code = models.IntegerField()
    Sub_Grade = models.CharField(max_length=2)

    def __str__(self):
        return self.Sub_Code

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(Student),
    ]