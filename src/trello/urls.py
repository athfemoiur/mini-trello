from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('secret-admin/', admin.site.urls),
    path('api/users/', include('users.urls', namespace='users')),
    path('sentry-debug/', trigger_error),
]
