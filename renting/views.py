from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import *

# Create your views here.

def car_detail(request, pk):
	car = get_object_or_404(Car, pk=pk)
	return render(request, 'car_detail.html', {'car': car})

def rent_new(request):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        cars = Car.objects.filter(status=1)
        context['car'] = cars
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {}
        return redirect('rent_new')

def get_data(request):
    try:

    except Exception:
        data = {
            'error': True,
        }

    return JsonResponse(data)
