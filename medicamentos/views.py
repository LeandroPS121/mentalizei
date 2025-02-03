from django.shortcuts import render

def medicamentos(request):
    return render(request, 'lista_med.html')