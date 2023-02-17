from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.floor} {self.number}'


class Acter(models.Model):
    Male = 'M'
    Female = 'F'
    GENDERS_CHOICES = [
        (Male, 'Мужчина'),
        (Female, 'Женщина'),
    ]    
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS_CHOICES, default=Male)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name    


class Director(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name    


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
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.DateField(null=True)
    budget = models.IntegerField(default=100000, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, related_name='movies')
    acters = models.ManyToManyField(Acter)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self) -> str:
        return self.name