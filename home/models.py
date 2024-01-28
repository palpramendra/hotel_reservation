from django.db import models

# Create your models here.
class Booking(models.Model):
    arrival_data=models.DateTimeField(auto_now_add=True)
    departure_date=models.DateTimeField(auto_now_add=True)
    adult=models.IntegerField(10)
    child=models.IntegerField(10)