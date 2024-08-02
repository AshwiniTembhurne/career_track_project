from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('applications/<int:id>/', views.application_details, name='application_details'),
    path('applications/new/', views.add_application, name='add_application'),
    path('applications/edit/<int:id>/', views.edit_application, name='edit_application'),
    path('applications/delete/<int:id>/', views.delete_application, name='delete_application'),
]
