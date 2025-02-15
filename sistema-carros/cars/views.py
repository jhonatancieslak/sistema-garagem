from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
         cars = cars.filter(model__icontains=search).order_by('model')

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )