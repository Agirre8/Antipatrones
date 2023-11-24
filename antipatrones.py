def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir entre cero."

def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return print("La suma da un total de: ", suma(num1, num2))
    elif operacion == 'resta':
        return print("La resta da un total de: ", resta(num1, num2))
    elif operacion == 'multiplicacion':
        return print("La multiplicación da un total de: ", multiplicacion(num1, num2))
    elif operacion == 'division':
        return print("La división da un total de: ",division(num1, num2))
    else:
        return "Operación no soportada."


#ahora tenemos una función para cada operacion para que la funcion calculadora lo tenga mas facil ya que solo tiene que llamar a las funciones anteriores
calcular("suma", 1, 2)


"""""

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

Este codigo tiene varias características de ser Spagheti Code
Manejo de errores: El código imprime un mensaje si la división entre cero ocurre, pero no detiene la ejecución o retorna nada
Anidamiento de condiciones: Al usar una serie de if sin un patrón claro de control de flujo, se crea una estructura complicada y difícil de segui
"""""