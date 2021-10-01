from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),

    ####################

    path('profile/', views.profile, name='profile'),
]
