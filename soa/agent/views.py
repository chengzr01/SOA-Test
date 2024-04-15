from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return JsonResponse({'code': 200, 'data': "Hello"}, status=200)
