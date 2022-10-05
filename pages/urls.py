# Marissa Wagner
# CIS 218
# 09/22/2022

from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView  

urlpatterns = [
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("projects/", AboutPageView.as_view(), name="projects"), 
    path("", HomePageView.as_view(), name="mwagner"),
]

