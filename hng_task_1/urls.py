from django.urls import path
from . import views

app_name = 'hng_task_1'

urlpatterns = [
    path('get_info', views.get_info, name='get_info'),
    path('api', views.get_info, name='get_info'),
]
