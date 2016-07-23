from django.shortcuts import render

# Create your views here.

From django.views.generic.base import TemplateView
Class LandingView(TemplateView):
	template_namae = "base/index.html"