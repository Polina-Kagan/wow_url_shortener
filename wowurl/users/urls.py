from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('reg', views.register, name='registration'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/logout.html', next_page='home', http_method_names=['get', 'post']), name='exit'),
    path('profile/', views.profile, name='profile'),

    
]
