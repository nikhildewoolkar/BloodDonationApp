from . import views
from django.urls import path
urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("adv/",views.adv,name="adv"),
    path("logout/",views.logout,name="logout"),
    path("fb/",views.fb,name="fb"),
    path("changepassword/",views.changepassword,name="changepassword"),
]