from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    film_turu= models.CharField(max_length=100,default=" ")
    aciklama = models.TextField()
    resim = models.CharField(max_length=100)







