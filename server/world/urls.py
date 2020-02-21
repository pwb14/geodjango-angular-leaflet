from django.conf.urls import url
from . import views

app_name = 'world'

urlpatterns = [
    url(r'^country/',
        views.CountriesDetailView.as_view(), name='countries-detail')
]