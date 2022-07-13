from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    number = models.IntegerField()
    address = models.CharField(max_length=50)
    group = models.CharField(max_length=10)
    district = models.CharField(max_length=30)
    age = models.IntegerField()
    photo = models.FileField()


class Message(models.Model):
    group = models.CharField(max_length=10)
    message = models.CharField(max_length=100)
    date = models.IntegerField()
    month = models.CharField(max_length=15)
    year = models.IntegerField()
    district = models.CharField(max_length=19)
    hospital = models.CharField(max_length=100)
