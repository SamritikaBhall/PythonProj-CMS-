from django.shortcuts import render
from MyLab.models import Student
# from django.shortcuts import messages
# Create your views here.
def Home(request):
    # messages.success(request, "this is submitted")
    return render(request, 'Home.html')
    

def Student(request):
    if request.method == "Post":
        Stu_id = request.Post.get('Stu_id')
        Stu_Fname = request.Post.get('Stu_Fname')
        Stu_Lname = request.Post.get('Stu_Lname')
        Stu_email = request.Post.get('Stu_email')
        Stu_Pass = request.Post.get('Stu_Pass') 
        Stu_dob = request.Post.get('Stu_dob') 
        Stu_grade = request.Post.get('Stu_grade') 
        Stu_marks = request.Post.get('Stu_marks')
        gender = request.Post.get('gender')  
        new_student = Student(Stu_id = Stu_id, Stu_Fname= Stu_Fname, Stu_Lname= Stu_Lname, Stu_email= Stu_email, Stu_Pass= Stu_Pass, Stu_dob = Stu_dob, Stu_grade= Stu_grade, Stu_marks= Stu_marks, gender = gender)
        Student.save()
        # messages.success(request, 'Profile details updated.')
    return render(request, 'Student.html')

def Staff(request):
    return render(request, 'Staff.html')

def Courses(request):
    return render(request, 'Courses.html')

def Subjects(request):
    return render(request, 'Subjects.html')