from django.urls import path
from authentification.views import *


urlpatterns = [
    path('login_user/',views.UserLoginView.as_view()),
    path('profile_user/',views.UserProfilesView.as_view()),
    path('logout_user/',views.UserLogoutView.as_view())
]