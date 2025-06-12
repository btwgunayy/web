from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.booking_form, name='booking_form'),
    path('success/', views.booking_success, name='booking_success'),
]