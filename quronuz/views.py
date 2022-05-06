from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    maruzas = Maruza.objects.order_by('-popular')[:5]
    return render(request , 'base.html' , {'maruzass':maruzas})

def qories(request):
    qori = Qori.objects.all()
    return render(request , 'qories.html' , {'qories':qori})

def qori(request, slug):
    qori = Qori.objects.get(slug=slug)
    sura = qori.sura_set.order_by()
    return render(request, "qori_detail.html", {
        'qori': qori,
        'suras': sura,
        })

def sura(request, slug):
    sura = Sura.objects.get(slug=slug)
    oyat = sura.oyat_set.order_by()
    return render(request, "sura_detail.html", {
        'suras': sura,
        'oyatlar':oyat,
        })



def domlalar(request):
    domla = Domla.objects.all()
    return render(request , 'domlalar.html' , {'domlalar':domla})

def domla(request, slug):
    domla = Domla.objects.get(slug=slug)
    maruza = domla.maruza_set.order_by()
    return render(request, "domla_detail.html", {
        'domla': domla,
        'maruzalar': maruza,
        })

def maruza(request, slug):
    maruza = Maruza.objects.get(slug=slug)
    return render(request, "maruza_detail.html", {
        'maruzalar': maruza,
        })