# Import necessary modules

from django.db import models

from django.urls import  reverse

class Rating(models.Model):
    Product = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    positive_review_number = models.IntegerField()
    negative_review_number = models.IntegerField()
    total_review = models.IntegerField()
    total_rating = models.FloatField()

