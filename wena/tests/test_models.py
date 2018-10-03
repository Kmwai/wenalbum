from django.test import TestCase

from wena.models import Location, Photo


class LocationModelTest(TestCase):
    def test_string_representation(self):
        location = Location(name='my location')
        self.assertEqual(str(location), location.name)

    def test_location_absolute_url(self):
        location = Location.objects.create(slug='slug')
        self.assertEquals(location.get_absolute_url(), '/slug/')


class PhotoModelTest(TestCase):
    def test_string_representation(self):
        photo = Photo(name='photo name')
        self.assertEqual(str(photo), photo.name)

    def test_photo_absolute_url(self):
        photo = Photo(id=1, slug='slug')
        self.assertEquals(photo.get_absolute_url(), '/1/slug/')