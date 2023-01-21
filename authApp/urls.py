from django.urls import path,include
from . import views
from .form import LoginForm
from django.contrib.auth import views as auth_view
from .form import ChangePasswordForm,ForgetPasswordForm,PasswordResetForm

urlpatterns = [
    path('',views.Registration.as_view(),name="index"),
    path('account/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),

    #profile
    path('Profile/',views.ProfileUpdate.as_view(),name='Profle'),

    #change Password
    path('PasswordChange/',auth_view.PasswordChangeView.as_view(template_name='changePassword.html',form_class=ChangePasswordForm,success_url='/changepasswordone/'),name="PasswordChange"),
    path('changepasswordone/',auth_view.PasswordChangeDoneView.as_view(template_name='done.html'),name='changepasswordone'),
    
    
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='resetPassword.html',form_class=ForgetPasswordForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='PasswordResetConfirm.html',form_class=PasswordResetForm),name='password_reset_confirm'),
    path('password-reset-complete',auth_view.PasswordResetCompleteView.as_view(template_name='done.html'),name='password_reset_complete'),
]
