from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.opening, name = 'opening'),
    path('validate_form', views.validate_form, name='validate_form'),
    path('success', views.success, name='success'),
    path('error', views.error, name='error')
]