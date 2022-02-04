from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the api index---hor!")


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
