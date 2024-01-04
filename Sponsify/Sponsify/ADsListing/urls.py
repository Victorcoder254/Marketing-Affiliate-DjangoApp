from .views import LandingPage, detailPage, partner_signup, account
from django.urls import path


urlpatterns = [
    path('', LandingPage, name= 'Home'),
    path('AD_detail/<int:pk>', detailPage, name= 'detail-Ad'),
    path('next/', partner_signup, name= 'nextNow'),
    path('nextup/', account, name= 'account'),
]