# Marissa Wagner
# CIS 218
# 09/22/2022


from django.test import TestCase

from django.test import SimpleTestCase
from django.urls import reverse  

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("mwagner"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("mwagner"))
        self.assertTemplateUsed(response, "mwagner.html")

    def test_template_content(self):  
        response = self.client.get(reverse("mwagner"))
        self.assertContains(response, "<h1>Marissa Wagner</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("projects"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("projects"))
        self.assertTemplateUsed(response, "projects.html")

    def test_template_content(self):  
        response = self.client.get(reverse("projects"))
        self.assertContains(response, "<h1>My Projects</h1>")

class ContactpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):  
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h1> </h1>")