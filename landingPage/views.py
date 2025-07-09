from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')
def features(request):
    return render (request, 'features.html')
def about(request):
    return render (request, 'about.html')
def soon(request):
    return render (request, 'soon.html')
