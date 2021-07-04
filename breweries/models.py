from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _


class BreweryTypes(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brewery Type'
        verbose_name_plural = 'Brewery Types'


class Breweries(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=150,
        unique=True,
    )

    website_url = models.URLField(
        verbose_name='Website URL',
        max_length=200,
        blank=True,
        null=True,
    )

    brewery_type = models.ForeignKey(
        BreweryTypes    ,
        verbose_name='Brewery type',
        on_delete=models.CASCADE,
    )

    city = models.CharField(
        verbose_name='City',
        max_length=150,
    )

    state = models.CharField(
        verbose_name='State',
        max_length=150,
        null=True,
        blank=True,
    )

    country = models.CharField(
        verbose_name='Country',
        max_length=150,
    )

    phone = models.CharField(
        verbose_name='Phone',
        max_length=15,
        blank=True,
        null=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False,
    )

    def get_absolute_url(self):
        return reverse('breweries:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brewery'
        verbose_name_plural = 'Breweries'
