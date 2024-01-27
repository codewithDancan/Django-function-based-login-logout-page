from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('reset', views.reset, name='reset'),
    path('sign-out', views.signout, name='sign_out'),
]
