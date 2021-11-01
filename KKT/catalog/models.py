from django.db import models

# Create your models here.

class CatalogModel(models.Model):
    #Fields
    id = models.AutoField(primary_key=True)
    rnk = models.IntegerField()
    