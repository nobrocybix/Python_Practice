from django.shortcuts import render

# Create your views here.
def index(request):
    '''學習筆記的主頁'''
    '''Home page of study notes'''
    return render(request, 'learning_logs/index.html')