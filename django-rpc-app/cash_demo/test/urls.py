from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/auth/', include('cash_user.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
