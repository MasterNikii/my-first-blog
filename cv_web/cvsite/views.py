from django.shortcuts import render

# Create your views here.
def cvsite(request):
        return render(request, 'cvsite/homepage.html')
