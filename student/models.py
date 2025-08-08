from django.db import models
from django.contrib.auth.models import User
from data_class.models import Class
from .code import generate_unique_code




class Student_info(models.Model):
 
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name = "Associated_Student",related_name="student")
    student_code = models.CharField(
        max_length=10,
        unique=True,
        default=generate_unique_code,
        editable=True,
        verbose_name="Student Code"
    )

    student_profile = models.ImageField(upload_to='student/',blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(verbose_name="student_age",blank=True,null=True)
    # student_class = models.IntegerField(verbose_name="student_class")
    email = models.EmailField(verbose_name="student_email")
    student_class = models.ForeignKey(Class,on_delete=models.CASCADE,verbose_name="student_class",null=True,blank=True)
    Roll_num = models.IntegerField(verbose_name="student_roll number",default=0,null=True,blank=True)
    refrence_code = models.CharField(verbose_name='refrence_code',default='n?A')
    joined = models.BooleanField(default=False,blank=True,null=True)
    
    # experimental ! 
    

    father_name = models.CharField(verbose_name='father_name',blank=True,null=True)
    mother_name = models.CharField(verbose_name='mother_name',blank=True,null=True)
    parent_contact = models.IntegerField(verbose_name='contact',blank=True,null=True)
    parent_email = models.EmailField(verbose_name='parent_email',blank=True,null=True)
    address  = models.TextField(verbose_name='Address',blank=True,null=True)
    emergency_contact = models.IntegerField(verbose_name='emergency conmtact',blank=True,null=True)



    class Meta:
        verbose_name = "student_info" 

    def __str__(self):
        return self.first_name  + " " +self.last_name



