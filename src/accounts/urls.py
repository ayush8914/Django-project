from django.urls import path
from django.urls import reverse_lazy
from .import views
from django.contrib.auth import views as auth_views
# from .import views

app_name = 'accounts'
urlpatterns =[
    path('', views.register_request, name="register"),
    path('login/', auth_views.LoginView.as_view() , name='login') ,
    path('accounts/login/', auth_views.LoginView.as_view() , name='login') ,
    path('logout/', auth_views.LogoutView.as_view() , name='logout') ,
    path('password_change/',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')) , name='password_change') ,
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') ,
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')) , name='password_reset') ,
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') ,
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),name='password_reset_confirm'),
    # path('' , views.register , name='register') ,
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_sucess.html'), name='password_reset_complete'),
     path('profile/', views.profile , name='profile') ,
    
#     accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
]