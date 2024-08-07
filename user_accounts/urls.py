from django.urls import path
from .views import signup_view, login_view, logout_view, admin_logout_view, logout_success, user_dashboard, admin_dashboard

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_logout/', admin_logout_view, name='admin_logout'),
    path('logout_success/', logout_success, name='logout_success'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]
