#Dogible\urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URL
    path('api/', include('dogapi.urls')),  # Include the dogapi URLs
]
