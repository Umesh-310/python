from django.shortcuts import render, redirect
from .models import Cars
from django.urls import reverse
# Create your views here.


def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        Cars.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            Cars.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('PK not found')
    else:
        return render(request, 'cars/delete.html')


def list(request):
    all_cars = Cars.objects.all()
    context = {'allCars': all_cars}
    return render(request, 'cars/list.html', context=context)
