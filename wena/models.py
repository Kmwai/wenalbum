from django.db import models
from django.utils import timezone
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = 'name',
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', args=[self.slug])


class Photo(models.Model):
    category = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='photos')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = (('id', 'slug'),)  # For querying photos by both id and slug (also to improve performance)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', args=[self.id, self.slug])
