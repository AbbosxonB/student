from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    y = Yunalish.objects.all()
    k = Kursi.objects.filter()
    g = Guruh.objects.all()
    return render(request, 'form.html', {
        'yunalishlar': y,
        'kurslar': k,
        'guruhlar': g,
    })

def get_kurslar(request):
    yunalish_id = request.GET.get('yunalish_id')
    kurslar = Kursi.objects.filter(guruh__yunalish__id=yunalish_id).distinct()
    data = [{'id': k.id, 'name': k.name} for k in kurslar]
    return JsonResponse({'kurslar': data})

def get_guruhlar(request):
    yunalish_id = request.GET.get('yunalish_id')
    kurs_id = request.GET.get('kurs_id')
    guruhlar = Guruh.objects.filter(
        yunalish__id=yunalish_id,
        kursi__id=kurs_id
    ).distinct()
    data = [{'id': g.id, 'name': g.name} for g in guruhlar]
    return JsonResponse({'guruhlar': data})

def get_fanlar(request):
    guruh_id = request.GET.get('guruh_id')
    fanlar = Fan.objects.filter(guruh__id=guruh_id).distinct()
    data = [{'id': f.id, 'name': f.name} for f in fanlar]
    return JsonResponse({'fanlar': data})

def saqlash(request):
    return render(request, 'test.html')