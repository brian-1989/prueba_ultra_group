from django.db import models

class City(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.CharField(max_length=20)
    city_name = models.CharField(max_length=20, unique=True)
    enable = models.BooleanField()