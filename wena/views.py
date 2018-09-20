from django.shortcuts import render, get_object_or_404
from .models import Location, Photo


def photo_list(request, location_slug=None):
    location = None
    locations = Location.objects.all()
    photos = Photo.objects.filter()
    if location_slug:
        location = get_object_or_404(Location, slug=location_slug)
        photos = locations.filter(location=location)
    return render(request, '', {'location': location,
                                'locations': locations,
                                'photos': photos})


def photo_detail(request, id, slug):
    photo = get_object_or_404(Photo, id=id, slug=slug)
    return render(request, '', {'photo': photo})




