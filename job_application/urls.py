from django.urls import path
from .views import application_list, application_details, add_application, edit_application, delete_application

urlpatterns = [
    path('applications/', application_list, name='application_list'),
    path('applications/<int:id>/', application_details, name='application_details'),
    path('applications/new/', add_application, name='add_application'),
    path('applications/edit/<int:id>/', edit_application, name='edit_application'),
    path('applications/delete/<int:id>/', delete_application, name='delete_application'),
]
