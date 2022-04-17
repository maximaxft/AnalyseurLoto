from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#from home.traitement import *
import home.traitement as calcul
# Create your views here.
object = calcul.GetValue()

def index(request):
    global object
    occurences = object.returnOccurencesNumero()

    chiffres = object.returnOccurencesChiffres()
    dixaines = object.returnOccurencesDixaines()
    vingtaines = object.returnOccurencesVingtaines()
    trentaines = object.returnOccurencesTrentaines()
    quarantaines = object.returnOccurencesQuarantaines()

    apparition_num = object.apparitionNumero(12)
    proba_par_num = object.probaParNumero(15)

    occurences.update(chiffres)
    occurences.update(dixaines)
    occurences.update(vingtaines)
    occurences.update(trentaines)
    occurences.update(quarantaines)
    occurences.update(apparition_num)
    occurences.update(proba_par_num)

    if request.method == 'POST':
        num = request.POST.get("numéro", "")
        if num:
            print("ici = {}".format(num))
            object = calcul.GetValue()
            apparition_num = object.apparitionNumero(int(num))
            occurences.update(apparition_num)
            return render(request, 'home/index.html', occurences)

    return render(request, 'home/index.html', occurences)

def index2(request):
    return render(request, 'home/index2.html')

@csrf_exempt
def compute2(request):
    global object
    num2 = int(request.POST.get("num2"))
    res2 = object.apparitionNumero(num2)

    return JsonResponse(res2)

@csrf_exempt
def compute1(request):
    global object
    num1 = int(request.POST.get("num1"))
    res1 = object.probaParNumero(num1)

    return JsonResponse(res1)