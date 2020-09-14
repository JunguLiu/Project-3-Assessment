from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addTask/', views.addTask, name='addTask'),
    path('deleteTask/<int:id>', views.deleteTask, name='deleteTask')
]
