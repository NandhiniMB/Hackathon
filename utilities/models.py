from django.db import models
from django.contrib.gis.db import models

class Utility_Category(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Utility Category"
        verbose_name        = "Utility_Categories"

  

class Utilities(models.Model):
     
    name = models.CharField(max_length=100)
    utility = models.ForeignKey(Utility_Category, blank=True, null=True, on_delete=models.PROTECT,)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Utility"
        verbose_name        = "Utilities"


# Create your models here.
