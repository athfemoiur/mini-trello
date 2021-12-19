from django.urls import path

from users.views import OTPView

app_name = 'users'

urlpatterns = [
    path('otp/', OTPView.as_view(), name='otp')
]