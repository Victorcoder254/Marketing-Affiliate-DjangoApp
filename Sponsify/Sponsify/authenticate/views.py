from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.first_name=firstname
        new_user.last_name=lastname
        new_user.save()
        return redirect('login')
    return render(request, 'authenticate/signupUser.html')

def createProfile(request):
    if request.method == 'POST':
            phone_number = request.POST.get('phnum')
            user_image = request.FILES.get('userimage')
            tt_account = request.POST.get('tiktok')
            yt_account = request.POST.get('youtube')
            ig_account = request.POST.get('instagram')
            fb_account = request.POST.get('facebook')
            
            logged_in_user =  request.user
            if logged_in_user.is_authenticated:
               user_profile = Profile.objects.create(user = logged_in_user, phone_number=phone_number,user_image=user_image, tt_account=tt_account,
                                                  yt_account=yt_account, ig_account=ig_account, fb_account=fb_account)
               user_profile.save()
               return redirect('Home')
            else:   
               return redirect('login')
    return render(request, 'authenticate/userProfile.html' )

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Check if the user has a profile
            try:
                profile = Profile.objects.get(user=user)
                return redirect('Home')  # Redirect to Home if the profile exists
            except Profile.DoesNotExist:
                return redirect('createProfile')  # Redirect to createProfile if the profile doesn't exist
        else:
            return HttpResponse("You are seeing this page because your login credentials are not correct!!")
          
    return render(request, 'authenticate/loginUser.html')


def logoutUser(request):
     logout(request)
     return redirect('login')
 