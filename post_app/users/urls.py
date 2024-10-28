from django.urls import path
from . import views

urlpatterns = [
        path('login/', views.sign_in,  name='login'),  # {'extend': 'base.html'},
        path('logout/', views.sing_out, name='logout'),
]