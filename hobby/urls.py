from django.urls import path
from hobby.views import HobbyViwe, CreateHobby, HobbyProgressViwe, CreateHobbyProgress

urlpatterns = [
    # path("hobby", HobbyViwe.as_view()),
    path("hobby/<int:pk>", HobbyViwe.as_view()),
    path("hobby", CreateHobby.as_view()),
    path("track-hobby/<int:pk>", HobbyProgressViwe.as_view()),
    path("track-hobby", CreateHobbyProgress.as_view()),
]
