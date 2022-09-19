from django.shortcuts import render
from .models import cvelement

# Create your views here.
def cvsite(request):
        cvelements = cvelement.objects.all()
        return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})
