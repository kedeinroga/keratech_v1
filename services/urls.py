from django.urls import path
from .views import ServicesPageView

services_patterns = [
    path('', ServicesPageView.as_view(), name="services"),
]