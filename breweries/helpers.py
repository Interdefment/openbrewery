from .models import Breweries, BreweryTypes


def clear_breweries_table():
    Breweries.objects.all().delete()


def create_brewery_types():
    types = [
        'micro',
        'nano',
        'regional',
        'brewpub',
        'large',
        'planning',
        'bar',
        'contract',
        'proprietor',
        'closed',
    ]
    for type in types:
        BreweryTypes.objects.get_or_create(
            name=type,
            defaults={'name': type}
    )


def create_brewery(brewery):
    brewery_type, _ = BreweryTypes.objects.get_or_create(
        name=brewery['brewery_type'],
        defaults={'name': brewery['brewery_type']},
    )

    Breweries.objects.create(
        name=brewery['name'],
        website_url=brewery['website_url'],
        brewery_type=brewery_type,
        city=brewery['city'],
        state=brewery['state'],
        country=brewery['country'],
        phone=brewery['phone'],
        updated_at=brewery['updated_at'],
        created_at=brewery['created_at'],
    )