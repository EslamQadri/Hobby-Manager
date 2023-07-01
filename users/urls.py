from django.urls import path
from users.views import UserSignup, UserLogin

urlpatterns = [
    path("signup", UserSignup.as_view()),
    path("login", UserLogin.as_view()),
]
