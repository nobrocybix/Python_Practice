from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    '''披薩的主頁'''
    '''Home page of pizza'''
    return render(request, 'pizzerias/index.html')

def pizzas(request):
    names = Pizza.objects.order_by("date_added")
    context = {'pizzas': names}
    return render(request, 'pizzerias/pizzas.html', context)

def pizza(request, pizza_id):
    name = Pizza.objects.get(id=pizza_id)
    entries = name.topping_set.order_by('-date_added')
    context = {'name': name, 'entries': entries}
    return render(request, 'pizzerias/pizza.html', context)