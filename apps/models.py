from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey('Region', models.CASCADE)

    def __str__(self):
        return self.name
