from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('login/', views.UserLogin, name = 'login'),
    path('login/auth/', views.UserLoginAuth, name = 'LoginAuth'),
    path('logout/', views.UserLogout, name = 'logout'),

    path('register/', views.UserRegister, name = 'register'),
    path('register/auth/', views.UserRegisterAuth, name = 'RegisterAuth'),
    path('register/<str:token>/activate/', views.UserRegisterActivate, name = 'RegisterActivate'),
    path('register/<str:link>/sender/', views.UserRegisterSend, name = 'RegisterSend'),

    path('register/validator/', views.UserRegisterValidator, name = 'RegisterValidator'),
]