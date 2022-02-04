from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('''
        Welcome to the Public Health Trends API. Current endpoints in development:
        \n 1) health_regions/ (retrieve all health regions)
        \n 2) forward_sortation_areas/ (retrieve all FSAs)
        \n 3) single_forward_sortation_area/ (retrieve a single FSA by its 3-character code)
    ''')


def health_regions(request):
    data = {
        'health_regions': [
            {
                'id': '1110',
                'name_en': 'Toronto Health',
                'name_fr': 'Toronto Health',
                'website_en': 'https://www.toronto.ca/community-people/health-wellness-care/',
                'website_fr': 'https://www.toronto.ca/community-people/health-wellness-care/'
            },
            {
                'id': '595',
                'name_en': 'Laval Health',
                'name_fr': 'Laval Health',
                'website_en': 'https://www.lavalensante.com/en/covid19/',
                'website_fr': 'https://www.lavalensante.com/covid19/'
            },
            {
                'id': '2406',
                'name_en': 'Vancouver Health',
                'name_fr': 'Vancouver Health',
                'website_en': 'http://www.vch.ca/covid-19',
                'website_fr': 'http://www.vch.ca/covid-19'
            },
            {
                'id': '499',
                'name_en': 'Halifax Health',
                'name_fr': 'Halifax Health',
                'website_en': 'https://novascotia.ca/coronavirus/',
                'website_fr': 'https://novascotia.ca/coronavirus/'
            }
        ]
    }
    return JsonResponse(data)


def forward_sortation_areas(request):
    data = {
        'forward_sortation_areas': [
            {
                'id': '1',
                'fsa': 'A0A',
                'health_regions': '1011',
                'estimated_pop': '8631',
            },
            {
                'id': '2',
                'fsa': 'A0B',
                'health_regions': '1011',
                'estimated_pop': '3066',
            },
            {
                'id': '3',
                'fsa': 'A0C',
                'health_regions': '1011',
                'estimated_pop': '32',
            },
            {
                'id': '4',
                'fsa': 'A0D',
                'health_regions': '1011',
                'estimated_pop': '1242',
            }
        ]
    }
    return JsonResponse(data)


def single_forward_sortation_area(request, fsa):
    data = {
        'id': 1,
        'fsa': fsa,
        'health_regions': '1011',
        'estimated_pop': '8631'
    }
    return JsonResponse(data)
