from django.shortcuts import render, get_object_or_404
from .models import Location, Photo


def photo_list(request, location_slug=None):
    """
    View function to display all the photos

    """
    location = None
    locations = Location.objects.all()
    photos = Photo.objects.all()
    if location_slug:
        location = get_object_or_404(Location, slug=location_slug)
        photos = photos.filter(location=location)
    return render(request, 'wena/photos/list.html', {'location': location,
                                                     'locations': locations,
                                                     'photos': photos})


def photo_detail(request, id, slug):
    """
    View function to display a single instance of a photo

    """
    photo = get_object_or_404(Photo, id=id, slug=slug)
    return render(request, 'wena/photos/detail.html', {'photo': photo})