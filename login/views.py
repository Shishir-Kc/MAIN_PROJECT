from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import Student_info
from teacher.models import Teacher
from django.contrib.auth.models import User,Group


def user_login(request):
    if request.method == "POST":
        user_code = request.POST.get('user_code')
        user_pass = request.POST.get('user_pass')

        try:
             try:
              student = Student_info.objects.get(student_code=user_code)
              user_name = student.user.username
             except Student_info.DoesNotExist:
               try: 
                 teacher = Teacher.objects.get(teacher_code = user_code)
                 user_name = teacher.user.username
               except Teacher.DoesNotExist:
                  messages.error(request,"user with that credentials does not exist ")
                  return redirect('login:login')
         
        except Student_info.DoesNotExist or Teacher.DoesNotExist:
            messages.error(request, "Failed to Login: Check your credentials!")
            return render(request, 'login/login.html')

       
        user = authenticate(username=user_name, password=user_pass)
        
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in scessfully ')
            if user.groups.filter(name='Student').exists():
             return redirect("student:student_dashboard")
            elif user.groups.filter(name='Teacher').exists():
               return redirect("teacher:teacher_dashboard")
        else:
            messages.error(request,'entered credentials are incorrect ! ')
            return redirect('login:login')
    
    return render(request, 'login/login.html')

def user_signup(request):
   if request.method == "POST":
     email = request.POST.get('email')
     first_name = request.POST.get('first_name')
     last_name = request.POST.get('last_name')
     password = request.POST.get('user_pass')
     refrence_code = request.POST.get('reference_code')
     user_image = request.FILES.get('profile_image')
     user_name = first_name+' '+last_name
     print(user_name)
     if not User.objects.filter(username=user_name).exists(): 
        user_account = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
        user_account.save()
        group = Group.objects.get(name='Student')  
        user_account.groups.add(group)
        user_std_account = Student_info.objects.create(user=User.objects.get(username=user_name),first_name=first_name,last_name=last_name,email=email,refrence_code=refrence_code,student_profile=user_image)
        user_std_account.save()
        messages.success(request,'You will have Acess To Your Account in a Short Period of time ! ')
        return redirect("login:login")

     else:
        messages.error(request,'username already exist !')

   return redirect('login:login')
      


@login_required
def user_logout(request):
   
   logout(request)
   return redirect("login:login")


def error_404(request,exception):
   return render(request,'error_404/404.html',status=404)


    
    