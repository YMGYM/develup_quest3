from django.urls import path
from . import views

app_name= "account"
urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('', views.loginchk, name="loginchk"),
    path('edituser/', views.edituser, name="edituser"),
    path('loginonly/', views.loginonly, name="loginonly"),
]
