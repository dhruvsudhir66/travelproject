from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='gallery')
    price = models.IntegerField()

    def __str__(self):
        return self.name
