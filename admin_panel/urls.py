from django.urls import path
from .views import admin_dashboard, admin_application_details, admin_add_application, admin_edit_application, admin_delete_application, user_list, user_edit, user_delete

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('application/<int:id>/', admin_application_details, name='admin_application_details'),
    path('add_application/', admin_add_application, name='admin_add_application'),
    path('edit_application/<int:id>/', admin_edit_application, name='admin_edit_application'),
    path('delete_application/<int:id>/', admin_delete_application, name='admin_delete_application'),
    # User management paths
    path('user-list/', user_list, name='user_list'),
    path('user-edit/<int:user_id>/', user_edit, name='user_edit'),
    path('user-delete/<int:user_id>/', user_delete, name='user_delete'),
]
