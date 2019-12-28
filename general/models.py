from django.contrib.gis.db import models as geo_models
from django.db import models
from django.contrib.auth.models import User


ROLE = (
    ('vendor', 'Vendor'),
    ('organizer', 'Organizer')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField()
    background = models.ImageField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    business_url = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE)
    attends = models.ManyToManyField('Event', related_name='attendees')
    follows = models.ManyToManyField('Event', related_name='followers')


class Venue(geo_models.Model):
    name = models.CharField(max_length=250)
    background = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250, default="US")
    zipcode = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
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
    description = models.TextField(blank=True, null=True)
    background = models.ImageField(blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    url = models.TextField()
    date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=EVENT_CATEGORY)
    reach = models.CharField(max_length=100, choices=REACH)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
