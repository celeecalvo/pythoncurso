# 1. Calcular el mayor de dos números ingresados 
# por teclado usando un operador ternario.

nro1 = int(input("Ingrese un numero: "))
nro2 = int(input("Ingrese otro numero: "))

nro_mayor = nro1 if nro1 > nro2 else "Ambos numeros son iguales" if nro2 == nro1 else nro2

print(nro_mayor)

# 2. Buscar una palabra en una lista ingresada por
# teclado usando args y un operador ternario.

def buscar_palabra(palabra_a_buscar, *args):
    return f"La palabra '{palabra_a_buscar}' " + ("está en la lista." if palabra_a_buscar in args else "no está en la lista.")

entrada = input("Ingresa palabras separadas por comas: ")  
lista_palabras = entrada.split(',')

palabra = input("¿Qué palabra quieres buscar? ")

resultado = buscar_palabra(palabra.strip(), *[p.strip() for p in lista_palabras])
print(resultado)

# 3. Determinar si un número es par o impar.

nro3 = int(input("Ingrese un numero: "))

par_impar = f"El numero {nro3} par" if nro3 % 2 == 0 else f"El numero {nro3} impar"

print(par_impar)

# 4. Calcular el promedio de una lista de números usando args y un operador ternario.

def calcular_promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

numeros = input("Ingresá números separados por comas: ") 
lista_numeros = [float(n.strip()) for n in numeros.split(',')]

promedio = calcular_promedio(*lista_numeros)
print(f"El promedio es: {promedio}")

# 5. Imprimir un mensaje de error si no se pasan suficientes argumentos.

def mostrar_datos(*args):
    mensaje = f"Se recibieron {len(args)} argumentos." if len(args) >= 3 else "Error: Se requieren al menos 3 argumentos."
    print(mensaje)

#ejemplos:
mostrar_datos()
mostrar_datos(2,22)
mostrar_datos(12, 'python', 2341, 'ejercicio')