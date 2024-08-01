from django.urls import path
from .views import signup_view, login_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]

# from . import views
# from django.urls import path

# urlpatterns = [
# path('', views.HomePage.as_view(), name='home'),
# ]