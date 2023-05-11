from django.db import models

# Create your models here.

class Dados(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.IntegerField(default=0)

class Labels(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=30)
