from django.db import models
from django.urls import reverse


class Location(models.Model):
    """
    Model representing a location (e.g Lisbon).
    """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = 'name',
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.name

    def get_absolute_url(self):
        """
        returns the url to a particular location instance
        """
        return reverse('wena:photo_list_by_location', args=[self.slug])


class Photo(models.Model):
    """
    Model representing a photo (but not a specific photo)
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='photos')
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
        """
        String for representing the Model object
        """
        return self.name

    def get_absolute_url(self):
        """
        returns the url of a particular photo instance
        """
        return reverse('wena:photo_detail', args=[self.id, self.slug])
