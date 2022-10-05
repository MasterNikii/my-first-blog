from django.shortcuts import render
from .models import Cucina, cvelement

# Create your views here.
def cvsite(request):
        cvelements = cvelement.objects.all()
        return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})
def contatti(request):
    return render(request, 'cvsite/contatti.html')
def curriculum(request):
        cucinas = Cucina.objects.all()
        return render(request, 'cvsite/curriculum.html', {'cucinas': cucinas})