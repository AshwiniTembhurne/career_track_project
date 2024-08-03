from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('applications/<int:id>/', views.admin_application_details, name='admin_application_details'),
    path('applications/new/', views.admin_add_application, name='admin_add_application'),
    path('applications/edit/<int:id>/', views.admin_edit_application, name='admin_edit_application'),
    path('applications/delete/<int:id>/', views.admin_delete_application, name='admin_delete_application'),
]
