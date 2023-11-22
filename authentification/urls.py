from django.urls import path
from authentification.views import *


urlpatterns = [
    path('login_user/', UserLoginView.as_view()),
    path('profile_user/', UserProfilesView.as_view()),
    path('logout_user/', UserLogoutView.as_view())
]