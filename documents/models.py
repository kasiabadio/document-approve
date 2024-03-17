from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=200)
    scope = models.CharField(max_length=200)
    responsible_person = models.CharField(max_length=200)
    accepting_person = models.CharField(max_length=200)
    is_validated = models.BooleanField(default=False)
