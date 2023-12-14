# urls.py
from django.urls import path
from .views import index, evaluation_request, login_view, register_view, admin_login, logout_view


app_name='evaluation'
urlpatterns = [
    path('', index, name='index'),
    path('evaluation_request/', evaluation_request, name='evaluation_request'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin/', admin_login, name='admin_login'),
    path('logout/', logout_view, name='logout'),
]