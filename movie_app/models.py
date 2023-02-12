from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Movie(models.Model):

    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'
    
    CURRENCY_CHOICES = [
        (RUB, 'Rubles'),
        (USD, 'Dollars'),
        (EUR, 'Euro'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.DateField(null=True)
    budget = models.IntegerField(default=100000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(args, **kwargs)


    def get_url(self):
        return reverse('movie-detail', args=[self.slug])


    def __str__(self) -> str:
        return self.name