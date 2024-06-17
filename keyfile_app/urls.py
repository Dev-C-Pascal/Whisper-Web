from django.urls import path
from . import views

urlpatterns = [
    path('save-key/', views.save_api_key, name='save_api_key'),
    path('success/', views.success, name='success'),

]
