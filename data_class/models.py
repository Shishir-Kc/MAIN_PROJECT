from django.db import models
from teacher import models as TD
import datetime

""""
    AUTHOR - MRC ! 


"""

class Subject(models.Model):
    name = models.CharField(max_length=50, verbose_name="Subject Name")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Class(models.Model):

    grade = models.CharField(verbose_name="Grade/Class")
    section = models.CharField(max_length=30, verbose_name="Section",blank=True,null=True)
    faculty = models.CharField(max_length=30,verbose_name="Faculty",default="N/A")
    subjects = models.ManyToManyField(Subject, verbose_name="Subjects")
    class_image = models.ImageField(upload_to='class_image/',blank=True,verbose_name="class_image")
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
   

    def __str__(self):

        return f"Grade = {self.grade}  Section = {self.section} Faculty = {self.faculty}"
    

class Assignments(models.Model):
    
    teacher = models.ForeignKey(TD.Teacher, on_delete=models.CASCADE,related_name='assignments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classs = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='notes_pdfs', null=True, blank=True)

    class Meta:
        verbose_name = "Assigment"
        verbose_name_plural = "Assigments"
        

    def __str__(self):
        return f"{self.title} - {self.classs} - {self.subject}"
    
    

class Project(models.Model):
    STATUS = [
        ('Approved','Approved'),
        ('Pending','Pending'),
        ('Rejected','Rejected'),

    ]
    student = models.ForeignKey('student.Student_info',on_delete=models.CASCADE,related_name="project")
    classs = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="project title")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(verbose_name="Project content")
    description = models.CharField(verbose_name="description",default="N/A")
    teacher_message = models.TextField(verbose_name='message form teacher',blank=True,null=True)
    status = models.CharField(choices=STATUS,verbose_name="Project Status",default="Pending")

    class Meta:
        verbose_name = "project"

    def __str__(self):
      return f"submitted by {self.student} {self.classs.grade} {self.classs.section} | Status {self.status}"
 


def get_current_year():

    return datetime.date.today().year

class YEAR_MONTH(models.Model):
    MONTH_CHOICES =[
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December')
]


    holiday = models.IntegerField(verbose_name='number_of_holiday')
    unexpected_holiday = models.IntegerField(verbose_name='unexpected_holidays')
    number_of_days = models.IntegerField(verbose_name='number_of_days_in_month')
    month = models.IntegerField(choices=MONTH_CHOICES, verbose_name="MONTH")
  
    current_year = models.IntegerField(default=get_current_year)  


    def __str__(self):
        return f"{self.month} {self.current_year}"


"""

    to do ! 

    1 )     make  the layout of partner program new like change the stats layout to upper  

    2) test the back end properly ! 

    3) make the backend flow proper - Done ! 

    4) add a option to upload student image from student dashboard not directly from login page !  - done

    5) make a proper class / Grade section  !  - Done

    6) add an option to change refrence code !  - Done 

    7) add middleware ! to check if user is logged in or not !  - Done

    8) add an ability to update the refrence code , only if teacher removes the student !  - Done

    9) ui improvements ! 

    10 ) add an option like to send a context msg why the teacher rejected the submitted project ! 

    11) add image upload limit for student max 200kb ! 
    
    12) fix images changes for teacher also ! 

    13) add a functionality for teacher : shorter project title , a btn to view full project detail , and an rejection description box where teacher will write whats wrong about student project !  - Done

    14) add a background worker ! for sending email ! w

    
    15) proper class filteration per school
    ! Max time this week ! 


    16) check for the class model and teacher model

    
    u better do it ! 


"""




