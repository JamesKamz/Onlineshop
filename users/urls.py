from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.Userlogin, name='login'),
    path('register/', views.UserSignup.as_view(), name='register'),
    path('logout/', views.Userlogout, name='logout'),
]
