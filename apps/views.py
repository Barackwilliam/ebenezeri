from django.shortcuts import render
from .models import TeamMember,New_Update,Course_Category,Popular_Course,Student_testimonial,Course_gallery,Service,User_Testimonial,Direct_Service
from django.contrib import messages
from .forms import MyMessage,Direct_Message_sevice
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import LogoLink


# Home Page
def home(request):
    team_members = TeamMember.objects.all()
    update = New_Update.objects.all()
    user_testimonial = User_Testimonial.objects.all()
    logo_link = LogoLink.objects.first() # Tunaleta moja tu


    context = {
        'team_members':team_members,
        'update':update,
        'user_testimonial':user_testimonial,
        'logo_link': logo_link
    } 
    return render(request, 'index.html',context)

# Elimu ya Ufahamu
def service(request):

    service = Service.objects.all()

    form = Direct_Message_sevice()
    logo_link = LogoLink.objects.first()  # Tunaleta moja tu

    ujumbe = ""

    if request.method == 'POST':
        form = Direct_Message_sevice(request.POST)
        if form.is_valid():
            form.save()
            ujumbe = "Hongera Ujumbe Wako Umetumwa Kikamilifu"

        else:
            form = Direct_Message_sevice() 
    context = {
        'form':form,
        'ujumbe':ujumbe,
        'service':service,
        'logo_link': logo_link
    }

    return render(request, 'service.html',context)

# Warsha za Kiroho
def contact(request):
    form = MyMessage(request.POST)
    logo_link = LogoLink.objects.first()  # Tunaleta moja tu

    ujumbe = ""


    if request.method == 'POST':
        form = MyMessage(request.POST)
        if form.is_valid():
            form.save()
            ujumbe = "Hongera Ujumbe Wako Umetumwa Kikamilifu"
        else:
            form = MyMessage()  
      
    context = {
        'form':form,
        'ujumbe':ujumbe,
        'logo_link': logo_link
    }
    return render(request, 'contact.html',context)




# Ushauri wa Kiroho
def counseling(request):
    logo_link = LogoLink.objects.first()  # Tunaleta moja tu

    return render(request, 'counseling.html',{'logo_link': logo_link})

# Ushuhuda wa Wateja
def About(request):
    logo_link = LogoLink.objects.first()  # Tunaleta moja tu

    return render(request, 'about.html',{'logo_link': logo_link})


@login_required(login_url='login')
def kozi(request):
    course_category = Course_Category.objects.all()
    popular_course = Popular_Course.objects.all()
    student_testimonial = Student_testimonial.objects.all()
    course_gallery = Course_gallery.objects.all()
    logo_link = LogoLink.objects.first()  # Tunaleta moja tu


    context = {
        'course_category':course_category,
        'popular_course':popular_course,
        'student_testimonial':student_testimonial,
        'course_gallery':course_gallery,
        'logo_link': logo_link

    }

    return render(request, 'courses_2.html',context)



def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
           if User.objects.filter(email=email).exists():
               messages.error(request, 'Pole..! Email hii Tayari imesajiliwa Tafadhari Tumia Email Nyingine.!')
               return redirect('Register')
           elif User.objects.filter(username=username).exists():
               messages.error(request, 'Loh Username uliyotumia ilisha sajiliwa Tafadhari Tumia Username Nyingine.!')
               return redirect('Register')
           else:
               user = User.objects.create_user(username=username, email=email, password=password2)
               user.save()
               messages.success(request,'Your Account created Successfully login below')
               return redirect('login')
            # #redirect usert to setting
               user_login = auth.authenticate(username=username, password=password)
               auth.login(request, user_login)
            #create a profile object for new user
               user_model = User.objects.get(username=username)
               new_profile = Profile.objects.create(user=user_model,role=user_model,address=user_model,phone=user_model,email=user_model,picture=user_model, bio=user_model)
               new_profile.save()
               return redirect('login')
        else:
            messages.error(request, 'password Not Matching')
            return render(request,'login.html')
    else:
        return render(request, 'Register.html')




# @login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login')
def pay(request):
    logo_link = LogoLink.objects.first()  # Tunaleta moja tu

    return render(request,'pay.html',{'logo_link': logo_link})




def login(request):
    if request.method =='POST':
       username = request.POST['username']
       password = request.POST['password']
       User = auth.authenticate(username=username, password=password)
       if User is not None: # type: ignore
          auth.login(request, User) # type: ignore
          return redirect('/')
       else:
        messages.error(request, 'Tafadhari ingiza Taarifa Sahihi na Ujaribu Tena au Jisajili Upya!')
        return redirect(login)
    else:
        return render(request, 'login.html')



def Debt(request):
    return render(request, 'PayTrack.html')
