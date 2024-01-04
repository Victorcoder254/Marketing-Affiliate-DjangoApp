from django.shortcuts import render, redirect
from ADsPartner.models import Listup
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from authenticate.models import Profile


def LandingPage(request):
    listings = Listup.objects.all()
    return render(request, 'home/LandingPage.html', {'listings': listings})

def detailPage(request, pk):
    listing = Listup.objects.get(pk=pk)
    
    if request.user.is_authenticated:
        return render(request, 'home/detail.html', {'listing': listing})
    else:
        return redirect('login')
    
def partner_signup(request):
    # Logout the user
    logout(request)
    
    # Redirect to the signup page of the next application
    return redirect('Signup')

def account(request):
    profile_user = Profile.objects.get(user=request.user)
    return render(request, 'home/Account.html', {'profile_user': profile_user})

