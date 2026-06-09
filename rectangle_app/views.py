from django.http import JsonResponse
from .rectangle import Rectangle

def rectangle_demo(request):
    rect = Rectangle(10, 5)

    result = [item for item in rect]

    return JsonResponse(result, safe=False)