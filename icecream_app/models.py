from django.db import models

class IceCreamShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    shop = models.ForeignKey(IceCreamShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.flavor




class Parent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
