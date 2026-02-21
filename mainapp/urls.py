from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('about/',views.about,name='about'),
    path("live/", views.sermons, name="live"),
    path('gallery_folders/', views.gallery_folders, name='gallery_folders'),
    path('gallery_folders/<int:folder_id>/', views.folder_images, name='folder_images'),
    path("contact/",views.contact,name="contact"),
    path("offerings/",views.offerings,name="offerings"),
]