from django.db import models


class TestAbstractModel(models.Model):
    class Meta:
        abstract = True
