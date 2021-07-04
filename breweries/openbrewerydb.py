import requests


class OpenBreweryException(Exception):
    def __init__(self, text):
        self.text = text


class OpenBreweryAPI:
    def __init__(self):
        self._base_url = 'https://api.openbrewerydb.org/breweries'

    def _request(
            self,
            url,
            params = None,
    ):
        session = requests.Session()
        request = requests.Request(
            'get',
            f'{self._base_url}{url}',
            params=params
        )
        prepared_request = request.prepare()

        print(f'OpenBreweryAPI params: {params}')
        response = session.send(prepared_request)

        if response.status_code != 200:
            raise OpenBreweryException(response.text)

        return response.json()

    def get_list(
        self,
        page = None,
        per_page = None,
        by_type = None,
        by_city = None,
    ):
        params = {}
        if page is not None:
            params['page'] = page
        if per_page is not None:
            params['per_page'] = per_page
        if by_type is not None:
            params['by_type'] = by_type
        if by_city is not None:
            params['by_city'] = by_city

        return self._request(url='/', params=params)
