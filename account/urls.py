from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # block below can be replaced with
    # path("", include("django.contrib.auth.urls"))
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', register, name='register'),

    # edit user profile
    path('edit/', edit, name='edit'),

    # social-auth
    path('social-auth', include('social_django.urls', namespace='social')),

    path('', dashboard, name='dashboard'),
]
