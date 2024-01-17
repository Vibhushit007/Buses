"""
URL configuration for bus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import os

from busapp1 import views

admin.site.site_header = "Blue Bus System Login Admin"
admin.site.site_title = "Blue bus Admin Portal"
admin.site.index_title = "Welcome to Blue Bus "


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("busapp1.urls")),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    # path('register/', views.register_view, name='register'),
]

STATIC_URL = 'static/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
