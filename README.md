# Antipatrones
# Ejercicio práctico: Identificación y refactorización de antipatrón "Spaghetti Code" en Python

Un antipatrón de programación es un patrón que puede ser considerado una mala práctica. "Spaghetti Code" es un antipatrón que se refiere a código con una estructura de control compleja, difícil de leer y seguir, generalmente debido a múltiples saltos de control, como instrucciones GOTO, ciclos y excepciones.

# Enunciado del ejercicio

Dada una porción de código Python escrita en estilo "Spaghetti Code", se te pide que identifiques las principales características de este antipatrón y refactorices el código para mejorar su legibilidad y mantenibilidad.

Considera el siguiente fragmento de código:


def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
Las funciones deberían tener una sola responsabilidad, y esta función tiene muchas. También se pueden observar problemas como la falta de modularización, uso de cadenas de texto para la lógica de control, y falta de manejo de errores.
