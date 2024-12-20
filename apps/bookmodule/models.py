from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    def __str__(self):
        return self.title
class Address(models.Model):
    city = models.CharField(max_length=90)
class Student(models.Model):
    name = models.CharField(max_length=90)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
