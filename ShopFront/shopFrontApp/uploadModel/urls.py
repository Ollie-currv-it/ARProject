# Add urls here
from django.urls import path
from uploadModel import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload_model/', views.upload_model, name='upload_model'),
]
