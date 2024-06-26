from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_register'),
    path('profile/', UserDetailView.as_view(), name='user_profile'),
]
