from django.shortcuts import render
from django.shortcuts import HttpResponse
 
def index(request):
    data= {'title': 'ГЛАВНАЯ СТРАНИЦА', 'values': ['some', 'thing', '123']}
    return render(request, "main/index.html", data)
