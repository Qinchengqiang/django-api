from django.db import models
# from enum import Enum
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    NSW = 'NSW'
    VIC = 'VIC'
    QLD = 'QLD'
    StateChoice = [
        (NSW, 'NSW'),
        (VIC, 'VIC'),
        (QLD, 'QLD'),
    ]

    id = models.AutoField(primary_key=True)  # primary key
    number = models.IntegerField(null=False, blank=False)
    street = models.CharField(max_length=500, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, choices=StateChoice, default=NSW)

    def __str__(self):
        return f"{self.number}, {self.street}, {self.city}, {self.state}"


class Person(models.Model):
    id = models.AutoField(primary_key=True)  # primary key
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.CharField(max_length=100, null=False, blank=False)
    address = models.ForeignKey(Address, related_name="persons", on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.name}, {self.email}"



