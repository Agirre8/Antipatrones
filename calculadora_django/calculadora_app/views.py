from django.shortcuts import render
from django.http import JsonResponse

def suma(request, num1, num2):
    resultado = int(num1) + int(num2)
    return render(request, 'calculadora_app/templates/calculadora_app/res_suma.html', {'resultado': resultado})

def resta(request, num1, num2):
    resultado = int(num1) - int(num2)
    return render(request, 'calculadora_app/templates/calculadora_app/res_resta.html', {'resultado': resultado})

def multiplicacion(request, num1, num2):
    resultado = int(num1) * int(num2)
    return render(request, 'calculadora_app/templates/calculadora_app/res_multiplicacion.html', {'resultado': resultado})

def division(request, num1, num2):
    try:
        resultado = int(num1) / int(num2)
        return render(request, 'calculadora_app/templates/calculadora_app/res_division.html', {'resultado': resultado})
    except ZeroDivisionError:
        return JsonResponse({'error': 'No se puede dividir entre cero'})
