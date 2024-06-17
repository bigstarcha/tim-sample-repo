from django.db import models

# Create your models here.
class Car(models.Model):
    id_number = models.IntegerField()
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_sedan = models.BooleanField()