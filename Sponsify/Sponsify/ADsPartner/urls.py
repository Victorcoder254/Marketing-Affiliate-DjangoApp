from .views import registration, loginUser, createProfile, ListAds, YourListings, dashboard, ADdetail, edit_Ad, delete_listing, edit_Profile
from django.urls import path


urlpatterns = [
    path('login/now/orNever/', loginUser, name= 'Login'),
    path('signup/', registration, name= 'Signup'),
    path('createProfile/', createProfile, name='createprofile'),
    path('ListAds/', ListAds, name='ListAds'),
    path('YourListings/<str:username>/', YourListings, name='YourListings'),
    path('Partner/dashboard/<str:username>/', dashboard, name='dashboard'),
    path('<int:pk>/', ADdetail, name='detail'),
    path('edit/<int:pk>/', edit_Ad, name='edit_listing'),
    path('delete/<int:pk>/', delete_listing, name='DeleteListing'),
    path('edit_profile', edit_Profile, name='Edit_profile'),
]