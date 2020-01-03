from datetime import datetime

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import *
from .models import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        qs = Event.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)

        date = self.request.GET.get('date')
        if date:
            qs = qs.filter(date__date=datetime.strptime(date, '%Y-%m-%d'))

        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category)
            
        venue_id = self.request.GET.get('venue')
        if venue_id:
            qs = qs.filter(venue_id=venue_id)

        return qs
