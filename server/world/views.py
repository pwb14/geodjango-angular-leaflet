from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import WorldBorder

# Create your views here.

class CountriesDetailView(View):
    def get(self, request):
        sm = WorldBorder.objects.get(name='Liberia')
        return JsonResponse(sm.mpoly.geojson, safe=False)