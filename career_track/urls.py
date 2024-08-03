from django.contrib import admin
from django.urls import path, include
from user_accounts.views import home, signup_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),  # Root URL directs to the home view
    path('jobs/', include('job_application.urls')),
    path('admin_panel/', include('admin_panel.urls')),
]
