from django.shortcuts import render
from .models import Cucina, cvelement
import mimetypes
import os
from django.http.response import HttpResponse
from django.http import Http404


# Create your views here.
def cvsite(request):
        cvelements = cvelement.objects.all()
        return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})
def contatti(request):
    return render(request, 'cvsite/contatti.html')
def curriculum(request):
        cucinas = Cucina.objects.all()
        return render(request, 'cvsite/curriculum.html', {'cucinas': cucinas})

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		# Modifica filename con il nome e l'estensione del file che vuoi far scaricare	
    filename = 'curriculumv.pdf'
    filepath = BASE_DIR + '/download/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def detail(request, cvelement_id):
    try:
        print('cv element id: %s' % cvelement_id)
    except cvelement.DoesNotExist:
        raise Http404("CV element does not exist")
    return render(request, 'cvsite/detail.html', {'element': cvelement_id})

