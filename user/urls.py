from django.urls import path
from .views import RegisterUser, submit

urlpatterns = [
    path('', RegisterUser.as_view()),
    path('submit', submit),
]

