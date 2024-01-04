from .views import signup, createProfile, loginUser, logoutUser
from django.urls import path


urlpatterns = [
    path('Authentication/LoginNow/', loginUser, name= 'login'),
    path('AuthenticateUserByAllowingRegistration/signupNowToHave125489/', signup, name= 'signup'),
    path('Authenticate1235/createProfileSinceItIsYourFirstTime/', createProfile, name='createProfile'),
    path('AuthenticateUserToLogoutOftheApplication/logoutBye!!Bye!!!User/', logoutUser, name='logout'),
]