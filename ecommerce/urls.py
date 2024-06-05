from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('sample/', views.sample, name='sample'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallerySingle/', views.gallerySingle, name='gallerySingle'),
    path('nature/', views.nature, name='nature'),
]
