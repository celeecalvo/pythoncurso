# 1. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
    
    
try:
    nro1 = int(input("ingrese un numero: "))
    nro2 = int(input("ingrese un numero: "))
    division = nro1 / nro2
    print(division)
except ZeroDivisionError:
    print("el segundo numero debe ser distinto de 0")
except Exception as e:
    print("Ha ocurrido un error {e}")
   
   
    
# 2. Escribe un programa que intente sumar un número y una cadena. Si se produce un error
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

try:
    nro = int(input("ingrese un numero: "))
    str = input("ingrese un numero: ")
    suma = nro + str
    print(suma)
except TypeError:
    print("Debe introducir dos numeros")
   
   
   

# 3. Escribe un programa que intente acceder a una clave que no existe en un
# diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

diccionario = { "nombre": "gato",
               "apellido": "gordo"
               }

try:
    print(diccionario["tipo"])
except KeyError as e:
    print("No existe la clave. Ha ocurrido un error {e}")
    
    
    
# 4. Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
# FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
# embargo, también intenta crear el archivo si no existe.

def abrir_archivo():
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)

def crea_archivo():
    with open("archivo.txt", "w") as arc:
        arc.write("Hola")
        print("Archivo creado.")

try:
    abrir_archivo()
except FileNotFoundError as nf:
    print("ERROR: {nf}")
    crea_archivo()
except Exception as e:
    print("Algo pasó... {e}")
    
    
    
# 5. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
# captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))

    resultado = num1 / num2
    print(resultado)

except ValueError:
    print("Ingrese un valor numérico.")
except ZeroDivisionError:
    print("El segundo número no debe ser cero.")
except Exception as e:
    print("Algo pasó: {e}")