from django.shortcuts import render, get_object_or_404
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


from random import sample
from .models import Test


def get_random_questions(fan_id):
    # Ma'lum fan bo'yicha 25 ta tasodifiy savol olish
    questions = Test.objects.filter(fan_id=fan_id)

    # Agar savollar soni 25 dan ko'proq bo'lsa, tasodifiy tanlash
    if questions.count() > 25:
        questions = sample(list(questions), 25)

    return questions

def start_test(request):
    if request.method == 'POST':
        fan_id = request.POST.get('fan_id')
        if not fan_id:
            return render(request, 'form.html', {
                'error': 'Fanni tanlang'
            })
        else:
            fan_id = int(fan_id)
            questions = get_random_questions(fan_id)
        return render(request, 'start_test.html', {
            'fan': fan_id,
            'questions': questions,
        })
    return render(request, 'form.html')

def test_views(request):
    print("Request method:", request.method)
    print("POST data:", request.POST)
    if request.method == 'POST':
        fan_id = request.POST.get('fan_id')
    else:
        fan_id = None

    return render(request, 'tests.html', {
        'fan': fan_id,
    })






