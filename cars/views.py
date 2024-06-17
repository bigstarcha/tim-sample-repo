from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Car
import json

# Create your views here.
@csrf_exempt
def create_car(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
    
        Car.objects.create(
            id_number = data.get('id_number'),
            manufacturer = data.get('manufacturer'),
            model = data.get('model'),
            year = data.get('year'),
            price = data.get('price'),
            is_sedan = data.get('is_sedan')
        )

        return HttpResponse('Car added successfully')
    else:
        return HttpResponse('Womp womp', status = 404)
    
def get_car(request, pk):
    if request.method == 'GET':
        car = Car.objects.get(pk=pk)

        car_json = {
            'id_number': car.id_number,
            'manufacturer': car.manufacturer,
            'model': car.model,
            'year': car.year
        }

        return JsonResponse(car_json, safe=False)
    else:
        return HttpResponse('Womp womp', status = 404)