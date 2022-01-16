from django.db import models

# Create your models here.


class Country(models.Model):

    # The longest country name: The United Kingdom of Great Britain and Northern Ireland
    name = models.CharField(max_length=56)
    # ~1 Billion
    population = models.IntegerField()
    image = models.TextField()

    class Meta:
        verbose_name = "Country Model"
