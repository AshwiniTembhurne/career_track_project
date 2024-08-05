from django.contrib import admin
from django.urls import path, include
from user_accounts.views import home, signup_view, login_view, logout_view, user_dashboard, admin_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL directs to the home view
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('jobs/', include('job_application.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    path('pages/', include('pages.urls')),  # Include the pages app URLs
]
