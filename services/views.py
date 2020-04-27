from django.views.generic.base import TemplateView
from django.shortcuts import render

class ServicesPageView(TemplateView):
    template_name = "services/services.html"