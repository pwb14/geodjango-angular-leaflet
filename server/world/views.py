from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.serializers import serialize

from .models import WorldBorder

# Create your views here.

class CountriesDetailView(View):
    def get(self, request):
        sm = serialize('geojson', WorldBorder.objects.all())
        # return JsonResponse(sm, safe=False)
        return HttpResponse(sm, content_type='json')


def points_view(request):
    points_as_geojson = serialize('geojson', Point.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')

def wojewodztwa_view(request):
    voivodeships_as_geojson = serialize('geojson', Voivodeship.objects.all())
    return HttpResponse(voivodeships_as_geojson, content_type='json')