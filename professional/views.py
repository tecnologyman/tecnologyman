from django.shortcuts import render

def professional_home(request):
    return render(request, 'professional/home.html')