from django.urls import path, include
from Users.views import RegisterView, LoginView, ProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
