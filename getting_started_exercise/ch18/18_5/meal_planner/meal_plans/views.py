from django.shortcuts import render

# Create your views here.
def index(request):
    '''膳食規劃的主頁'''
    '''Home page of meal plan'''
    return render(request, 'meal_plans/index.html')