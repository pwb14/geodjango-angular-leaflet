from django.conf.urls import url
from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'world'

router = routers.DefaultRouter()
router.register(r'labels', views.CountriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^country/',
        views.CountriesDetailView.as_view(), name='countries-detail'),
    
]