from django.shortcuts import render

def creator_home(request):
    return render(request, 'creator/home.html')