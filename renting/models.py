from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    AVAILABLE = 1
    LEASED = 2
    BOOKED = 3

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (LEASED, 'Leased'),
        (BOOKED, 'Booked')
    )

    license_plate = models.CharField('License ID', max_length=10, blank=False, primary_key=True)
    doors = models.IntegerField('Doors')
    diesel = models.BooleanField()
    status = models.IntegerField("Status", choices=STATUS_CHOICES,
                                 default=AVAILABLE)
    size = models.CharField('Car Size', max_length=10, blank=False)
    services = models.ManyToManyField(Client, through='Rent')

    def __str__(self):
        return self.license_plate

class Rent(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    since = models.TimeField()
    until = models.TextField()
    history_comments = models.TextField()

    class Meta:
        unique_together = (("client", "car"),)

    def __str__(self):
        return self.client.id + " " + self.car.license_plate + " " + self.date