from django.db import models

# Create your models here.
class test(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    custom_id = models.CharField(max_length=100)

class toggle(models.Model):
    shopname = models.CharField(max_length=100)
    toggle_value = models.BooleanField(default=0)

    def __str__(self):
        return f'toggle #{self.id}'
    
class Shop(models.Model):
    shopname = models.CharField(max_length=100)
    count = models.IntegerField(default=0)  