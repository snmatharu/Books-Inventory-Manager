from django.urls import path

from . import views

urlpatterns = [
    
    path('update/', views.AddData, name='AddData'),
    path('', views.GetData, name='GetData'),
]