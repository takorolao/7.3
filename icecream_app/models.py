from django.db import models
from django.core.validators import RegexValidator

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
    a = models.IntegerField(validators=[RegexValidator(r"^[0-9]?$")])   
    b = models.IntegerField() 

    def __str__(self):
        return self.name
    
    def newmethod(self):
        return str(self.pk)  + " " + self.name
    
    def sum(self):
        return self.a + self.b


class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
