from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    review = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name