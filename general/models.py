from django.contrib.gis.db import models as geo_models
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    background = models.ImageField()
    profile = models.ImageField()
    short_description = models.TextField()
    business_url = models.CharField(max_length=255)
    attends = models.ManyToManyField('Event', related_name='attendees')
    follows = models.ManyToManyField('Event', related_name='followers')


class Venue(geo_models.Model):
    name = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    description = models.TextField()
    lon = models.FloatField()
    lat = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


EVENT_CATEGORY = (
    ('artsy', 'Artsy'),
    ('boozey', 'Boozey'),
    ('charity', 'Charity'),
    ('craftsy', 'Craftsy'),
    ('foody', 'Foody'),
    ('musicy', 'Musicy'),
    ('petsy', 'Petsy')
)

REACH = (
    ('local', 'Local'),
    ('regional', 'Regional'),
    ('national', 'National')
)

class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    background = models.ImageField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    url = models.TextField()
    date = models.DateTimeField()
    sale_date = models.DateTimeField()
    category = models.CharField(max_length=100, choices=EVENT_CATEGORY)
    reach = models.CharField(max_length=100, choices=REACH)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
