# Marissa Wagner
# CIS 218
# 09/22/2022

from django.shortcuts import render

from django.http import HttpResponse

# def homePageView(request):
#    return HttpResponse("Hello, World!")

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "mwagner.html"

class AboutPageView(TemplateView): 
    template_name = "projects.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"