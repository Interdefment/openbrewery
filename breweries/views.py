from django.http import HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from . import helpers
from .models import Breweries

from breweries.openbrewerydb import OpenBreweryAPI, OpenBreweryException


class HomeView(TemplateView):
    template_name = 'breweries/index.html'


class BreweriesListView(ListView):
    model = Breweries
    paginate_by = 20


class BreweriesDetailView(DetailView):
    model = Breweries


class BreweriesDeleteView(DeleteView):
    model = Breweries
    success_url = reverse_lazy('breweries:list')


class BreweriesCreateView(CreateView):
    model = Breweries
    fields = (
        'name',
        'website_url',
        'brewery_type',
        'city',
        'state',
        'country',
        'phone',
    )


class BreweriesUpdateView(UpdateView):
    model = Breweries
    fields = (
        'name',
        'website_url',
        'brewery_type',
        'city',
        'state',
        'country',
        'phone',
    )


def download_data(request):
    per_page = request.GET.get('per_page')
    page = request.GET.get('page')
    by_type = request.GET.get('by_type')
    by_city = request.GET.get('by_city')

    if request.GET.get('clear_all', 'false') == 'true':
        helpers.clear_breweries_table()

    breweries_api = OpenBreweryAPI()
    try:
        breweries = breweries_api.get_list(
            per_page=per_page,
            page=page,
            by_type=by_type,
            by_city=by_city,
        )
    except OpenBreweryException:
        return HttpResponseServerError('Not today')


    for brewery in breweries:
        helpers.create_brewery(brewery)

    return render(request, 'breweries/index.html')
