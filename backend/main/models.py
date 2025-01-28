from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def short_price (self):
        if self.price == int(self.price):
            return f"{int(self.price)}$"
        else:
            return f"{self.price}$"

    def short_description(self):
        if len(self.description) > 75:
            return self.description[:75].rsplit(' ', 1)[0] + '...'
        return self.description

    def __str__(self):
        return self.title

class Action(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='actions/')

    def short_description(self):
        if len(self.description) > 75:
            return self.description[:75].rsplit(' ', 1)[0] + '...'
        return self.description

    def __str__(self):
        return self.title
