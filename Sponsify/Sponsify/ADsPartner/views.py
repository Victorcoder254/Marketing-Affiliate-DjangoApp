from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import BusinessProfile, Listup
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group


def registration(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.first_name=firstname
        new_user.last_name=lastname   
        job_lister_group, created = Group.objects.get_or_create(name='JobLister')
        new_user.groups.add(job_lister_group)
        new_user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Authenticate the user
            return redirect('createprofile')  # Redirect to profile creation page
        else:
            return HttpResponse('Failed to log in after registration.')

    return render(request, 'partner/signup.html')    


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.groups.filter(name='JobLister').exists():
                try:
                    BusinessProfile.objects.get(business=user)
                except ObjectDoesNotExist:
                    return redirect('createprofile')
                else:
                    return redirect('dashboard', username=request.user.username)
            else:
                return redirect('dashboard', username=request.user.username)
        else:
            return redirect('Login')
    
    return render(request, 'partner/login.html')


def createProfile(request):
    if request.method == 'POST': 
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        industry = request.POST.get('industry')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact_email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        website = request.POST.get('website')
        social_media_link = request.POST.get('social')

        log_in_user = request.user
        
        # Make sure the user is authenticated before creating the profile
        if log_in_user.is_authenticated:
            businessProfile = BusinessProfile.objects.create(
                business=log_in_user,
                name=name,
                photo=photo,
                industry=industry,
                description=description,
                location=location,
                contact_email=contact_email,
                phone_number=phone_number,
                website=website,
                social_media_link=social_media_link
            )
            businessProfile.save()
            return redirect('dashboard', username=log_in_user.username) 
        else:
            # Handle the case where the user is not authenticated
            return HttpResponse("User is not authenticated.")
    
    return render(request, 'partner/CreateProfile.html')



@login_required
def ListAds(request):
    if request.method == 'POST':
        product = request.FILES.get('pro_image')
        description = request.POST.get('description')
        specifications = request.POST.get('specifics')
        price_offers = request.POST.get('price')
        contact_info = request.POST.get('contact')
        if request.user.groups.filter(name='JobLister').exists():
           logged_in_user = request.user
           Listnow = Listup.objects.create(adlisting=logged_in_user, product=product, description=description,
                                        specifications=specifications, price_offers=price_offers, contact_info=contact_info)
           Listnow.save()
           username = request.user.username
           return redirect('YourListings', username=username)
        else:
           return HttpResponse("You don't have permission to access this page.")
    return render(request, 'partner/Listup.html')

@login_required
def YourListings(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.user != user:
        return HttpResponse("Login")
    
    listings = Listup.objects.filter(adlisting=user)
    return render(request, 'partner/YourListings.html', {'listings': listings})

@login_required
def dashboard(request, username):
    user = get_object_or_404(User, username=username)
    if request.user != user:
          return HttpResponse("You don't have permission to access this page.")
    
    profile = None  # Initialize profile variable
    total = 0       # Initialize total variable
    
    if request.user.groups.filter(name='JobLister').exists():
        profile = BusinessProfile.objects.get(business = user)
        total = Listup.objects.filter(adlisting=user).count() 
    return render(request, 'partner/Dashboard.html', {'profile': profile, 'total': total})


def ADdetail(request, pk):
    detail = Listup.objects.get(id=pk)
    username = detail.adlisting.username
    return render(request, 'partner/ADdetail.html', {'detail': detail, 'username': username, 'pk': pk})

@login_required
def edit_Ad(request, pk):
    listing = get_object_or_404(Listup, pk=pk)
    if request.method == 'POST':
        new_product = request.FILES.get('pro_image')
        if new_product:
            listing.product = new_product
        
        listing.description = request.POST.get('description', listing.description)
        listing.specifications = request.POST.get('specifics', listing.specifications)
        listing.price_offers = request.POST.get('price', listing.price_offers)
        listing.contact_info = request.POST.get('contact', listing.contact_info)
        listing.save()
        return redirect('detail', pk=pk)

    return render(request, 'partner/edit_listing.html', {'listing': listing})

def delete_listing(request, pk):
    # Retrieve the listing object or return a 404 error if not found
    listing = get_object_or_404(Listup, pk=pk)

    # Check if the logged-in user is the owner of the listing (optional, if needed)
    if request.user != listing.adlisting:
        return HttpResponse("You don't have permission to delete this listing.")

    # Delete the listing
    listing.delete()

    # Redirect to a page after deletion, like the user's listings page
    return redirect('YourListings', username=request.user.username)

def edit_Profile(request):
    profile = BusinessProfile.objects.get(business=request.user)
    if request.method == 'POST': 
        new_photo = request.FILES.get('photo')
        if new_photo:
            profile.photo = new_photo
        profile.name = request.POST.get('name', profile.name)
        profile.industry = request.POST.get('industry',profile.industry )
        profile.description = request.POST.get('description', profile.description)
        profile.location = request.POST.get('location', profile.location)
        profile.contact_email = request.POST.get('email', profile.contact_email )
        profile.phone_number = request.POST.get('phone',  profile.phone_number )
        profile.website = request.POST.get('website', profile.website )
        profile.social_media_link 
        

        profile.save()
        return redirect('dashboard', username=request.user.username) 
    
    return render(request, 'partner/edit_profile.html')
