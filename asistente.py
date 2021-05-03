#!/bin/python

import time
import os
import sys
import base64

os.system("clear")
def slowprint(s):
        for p in s + '\n':
            sys.stdout.write(p)
            sys.stdout.flush()
            time.sleep(1./500)
print("Instalando paquetes")
def hola():
	
	os.system("figlet -f small Asistente | lolcat")
	print("                   \033[1;32mby:\033[1;0m Jocker Termux")
	slowprint("""
..................:::menu:::...............
\033[1;31m[\033[1;0m1\033[1;31m]\033[1;0m Ayuda en bash
\033[1;31m[\033[1;0m2\033[1;31m]\033[1;0m Ayuda en python
\033[1;31m[\033[1;0m3\033[1;31m]\033[1;0m Clonar sitios web
\033[1;31m[\033[1;0m4\033[1;31m]\033[1;0m Codificar texto con base64
\033[1;31m[\033[1;0m5\033[1;31m]\033[1;0m Descodificar
\033[1;31m[\033[1;0m6\033[1;31m]\033[1;0m Escanear web con nmap
\033[1;31m[\033[1;0m7\033[1;31m]\033[1;0m Info. de los paquetes
\033[1;31m[\033[1;0m8\033[1;31m]\033[1;0m Traductor
\033[1;31m[\033[1;0m9\033[1;31m]\033[1;0m Descargar curso bash
\033[1;31m[\033[1;0m10\033[1;31m]\033[1;0m Descargar curso python
\033[1;31m[\033[1;0m11\033[1;31m]\033[1;0m Termux
\033[1;31m[\033[1;0m12\033[1;31m]\033[1;0m Usar sqlmap
\033[1;31m[\033[1;0m13\033[1;31m]\033[1;0m EmailSpoofing

\033[1;31m[\033[1;0m00\033[1;31m]\033[1;0m Salir
\033[0m
.........................................""")
	print("")
	opc = int(input("opcion ---> "))
	print("")
	if opc == 1:
		slowprint("Esperando respuestas....")
		time.sleep (1)
		slowprint("Listo")
		slowprint("Ahora solo escribe el comando 'cat bash.txt'")
		os.system('mv todo/.bash.txt bash.txt')
		hola()
	elif opc == 2:
		slowprint("Esperando respuestas....")
		time.sleep (1)
		slowprint("\033[32m[!] Listo")
		slowprint("Ahora solo escribe el comando 'cat python.txt'")
		os.system('mv todo/.python.txt python.txt')
		hola()
	elif opc == 3:
		os.system("python todo/.clon.py")
	elif opc == 4:
		os.system("figlet -c Codificador")
		text = input( '\033[31mTexto a codificar ---> ' )
		time.sleep(0.1)
		texto_bytes = base64.b64encode(text.encode())
		textocod =texto_bytes.decode()
		print("")
		print('\033[31m su texto codificad base64 es: '+textocod)
		print("")
		time.sleep(3)
		hola()
	elif opc == 5:
		os.system("figlet -c Descodificador")
		texto = input('\033[35mtexto en base64 --->  ')
		texto_encode = base64.b64decode(texto.encode())
		res=(texto_encode.decode())
		print("")
		print("\033[32m Su Texto Es: " +res)
		time.sleep(3)
		print("")
		hola()
	elif opc == 6:
		os.system("clear")
		nmap = input("Web a escanear(ejemplo: https://www.google.com) ---> ")
		print("\033[32m[*]\033[39m "+nmap)
		print("\033[32m[!]\033[39m Escaneando...")
		os.system("nmap -v -A "+nmap)
		time.sleep(1)
		hola()
	elif opc == 7:
		os.system("bash todo/.paqs")
		os.system("clear")
		hola()
	elif opc == 8:
		os.system("python todo/.traductor")
		hola()
	elif opc == 9:
		os.system("bash todo/.bash")
	elif opc == 10:
		os.system("bash todo/.python")
	elif opc == 11:
		os.system("bash todo/.termux")
	elif opc == 12:
		os.system("bash todo/.sqlmap")
	elif opc == 13:
		os.system("python todo/.emailspoof")
	elif opc == 00 or 0:
		os.system('clear')
		os.system("cd $HOME")
		exit()
	elif opc == "" or " ":
                        print("\033[1;31m")
	os.system("figlet -f small ERROR")
	print("\033[31mERROR ENTRADA NO VALIDA ELIJA UNA OPCION\033[0m")
	hola()
hola()
