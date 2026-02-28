from django.shortcuts import render

# Placeholder views for users app

def index(request):
    return render(request, 'users/index.html')
