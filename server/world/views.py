from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.serializers import serialize
from django.core.cache import cache
from rest_framework import viewsets

from .models import WorldBorder
from .serializers import WorldBorderSerializer

# Create your views here.

class CountriesDetailView(View):
    def get(self, request):
        redis_key = 'counties'
        countries = cache.get(redis_key)
        print(WorldBorder.objects.filter(name='Liberia'))
        sm = serialize('geojson', WorldBorder.objects.filter(name='Liberia'))
        print(type(sm))
        # sm = serialize('geojson', WorldBorder.objects.all())
        return HttpResponse(sm, content_type='json')

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
