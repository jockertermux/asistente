import os, time

os.system("clear")
print("+\033[1;0m")
os.system("figlet -f small CloneWeb | lolcat")
url = input("URL de la pagina --> ")

if url == "":
	print("\e[1;31mERROR! Debes colocar la URL\e[1;39m")

else:
	name = input( "Nombre del archivo --> ")


	print("\033[1;32m[*]\033[1;39m Pagina: "+url)
	print("\033[1;32m[*]\033[1;39m Filename: "+name)
	print("\033[1;32m[*]\033[1;39m Espera...")
	os.system("wget "+url+" -o "+name)
	print("\033[1;32m[!]\033[1;39m Listo,La pagina clonada se va a la carpeta 'webs'")
	time.sleep(1)
	os.system("mv "+name+" webs")
	os.system("python asistente.py")
