"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import HomeView, TagView, PerformanceView, index_view
urlpatterns = [
    path('', index_view),
    path('api/v1/tag',TagView.as_view(), name="tag_view"),
    path('api/v1/performance',PerformanceView.as_view(), name="performance_view"),
    path('api/v1/home', HomeView.as_view(), name="home_view"),
]
