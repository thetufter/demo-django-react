from django.db import models

class Person(models.Model):
    name = models.CharField("Name", max_length=512)
    email = models.EmailField("Email Address", max_length=254)
