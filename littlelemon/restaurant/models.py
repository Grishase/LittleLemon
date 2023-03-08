from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price =models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.SmallIntegerField()

    def get_item(self):
        return f"{self.title}: {self.price}"
    
class Booking(models.Model):
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    bookingdate=models.DateField()

    def __str__(self):
        return f"Name of the Customer:{self.name} ,{self.no_of_guests} People, Date: {self.bookingdate}"