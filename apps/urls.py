
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('About/', views.About, name='About'),
    path('contact/', views.contact, name='contact'),
    path('kozi/', views.kozi, name='kozi'),
    path('About/', views.About, name='About'),
    path('About/', views.About, name='About'),
    path('About/', views.About, name='About'),
    path('logout/', views.logout, name='logout'),
    path('Register/', views.Register, name='Register'),
    path('login/', views.login, name='login'),
    path('pay/', views.pay, name='pay'),
    path('Debt/', views.Debt, name='Debt'),
   
]
