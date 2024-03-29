from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', login_form, name='login'),
    path('logout/', logout_user, name='logout'),
    
    path('delete/<int:uid>', delete_account, name="delete_account"),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]