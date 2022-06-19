from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    Phone_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} Teacher'


class Courses(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    course_name = models.CharField(max_length=70)
    Year = models.DateTimeField(auto_now=True)
    file=models.FileField(null=True,blank=True)
    def __str__(self):
        return f'{self.course_name} Course'


class Classes(models.Model):
    MY_CHOICES = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    )
    class_name =  models.CharField(max_length=1, choices=MY_CHOICES)
    # course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    course=models.ManyToManyField(Courses)
    Teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    # student_id=models.ManyToManyField(Student)
  
    def __str__(self):
        return f'{self.class_name} Class'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classs=models.ForeignKey(Classes,on_delete=models.CASCADE)
    Phone_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} Student'

class Result(models.Model):
    Result = models.CharField(max_length=70)
    Marks =  models.PositiveIntegerField()
    Totall_Marks =  models.PositiveIntegerField()
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.student_id.user.username} Result'


class Quiz(models.Model):
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    classs=models.ForeignKey(Classes,on_delete=models.CASCADE)
    file=models.FileField(null=True)
    submit_file=models.FileField(null=True,blank=True)
    def __str__(self):
        return f'{self.course_id} Quiz'



class Assignment(models.Model):
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    classs=models.ForeignKey(Classes,on_delete=models.CASCADE)
    file=models.FileField(null=True)
    submit_file=models.FileField(null=True,blank=True)
    def __str__(self):
        return f'{self.course_id} Assignment'



class Notifications(models.Model):
    Teacher_id=models.OneToOneField(Teacher, on_delete=models.CASCADE)
    classs=models.ForeignKey(Classes,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return f'Teacher :{self.Teacher_id} class {self.classs} Notification'


class Contact(models.Model):
    Name = models.CharField(max_length=500)
    Email = models.TextField()
    Subject = models.CharField(max_length=500)
    Message = models.CharField(max_length=500)
    def __str__(self):
        return self.Name




