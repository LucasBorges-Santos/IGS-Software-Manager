from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('get_employees', views.get_employees, name='get_employees'),
    path('create_employee', views.create_employee, name='create_employee'),
    path('delete_employee', views.delete_employee, name='delete_employee')
]