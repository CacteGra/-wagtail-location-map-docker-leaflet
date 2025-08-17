# Replace from django.db import models with the next line
# so that we use geodjango models
from django.contrib.gis.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)
