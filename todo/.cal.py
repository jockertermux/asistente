import os 
import time
import sys


print('''
..........:::Calculadora:::..........
1. Sumar
2. Restar
3. Multiplicar
4. Dividir

5. Salir
.....................................
    ''')
opc = int(float(input("opcion --->")))
if opc == 1:
        n1 = int(float(input("Primer numero a sumar: ")))
        n2 = int(float(input("Segundo numero a sumar: ")))
        print("El resultado es: ")
        respuesta = n1+n2
        print(respuesta)
        time.sleep(2)
        os.system("python todo/.cal.py")
elif opc == 2:
        n1 = int(float(input("Primer numero a sumar: ")))
        n2 = int(float(input("Segundo numero a restar: ")))
        print("El resultado es: ")
        respuesta = n1-n2
        print(respuesta)
        os.system("python todo/.cal.py")
elif opc == 3:
        n1 = int(float(input("Primer numero a multiplicar: ")))
        n2 = int(float(input("Segundo numero a multiplicar: ")))
        print("El resultado es: ")
        respuesta = n1*n2
        print(respuesta)
        time.sleep(2)
        os.system("python todo/.cal.py")
elif opc == 4:
        n1 = int(float(input("Primer numero a dividir: ")))
        n2 = int(float(input("Segundo numero a dividir: ")))
        print("El resultado es: ")
        respuesta = n1/n2
        print(respuesta)
        time.sleep(2)
	os.system("python todo/.cal.py")
elif opc == 5:
        os.system('bash todo/.termux')
else:
        print("ERROR! Escoga solo un numero del menu")
        os.system("python todo/.cal.py")
