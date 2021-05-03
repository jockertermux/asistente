#!/bin/bash
#creditos a DeepSociety xd
		W='\033[1;0m'
		R='\033[1;31m'
                G='\033[1;32m'
                Y='\033[1;33m'
                B='\033[1;34m'
                M='\033[1;35m'
                C='\033[1;36m'
                W='\033[0m'
menu(){
clear
figlet -f small cursos bash | lolcat
echo -e "$R [$W 1$R ]$W Curso bash 1"
echo -e "$R [$W 2$R ]$W Curso bash 2"
echo -e "$R [$W 3$R ]$W Curso bash 3"
echo ""
echo -e "$R [$W 00$R ]$W Back to main menu"
echo ""
read -p "Eliga una opcion ---> " men

if [ $men == "1" ];then
echo -e "Ruta a mover el curso $C ($W ejemplo:$G /sdcard$C): "
read -p ">>> " mov
echo -e "$G [*] Descargando..."
wget http://www.informatica.us.es/~ramon/articulos/Programacion-BASH -O curso-bash-1.pdf -o log
rm log
mv curso-bash-1.pdf $mov
echo -e "$W Descarga completa,Moviendo curso a $mov"
sleep 1
menu

elif [ $men == "2" ];then
echo -e "Ruta a mover el curso $C ($W ejemplo:$G /sdcard$C): "
read -p ">>> " mov
echo -e "$G [*] Descargando..."
wget http://www.edu.xunta.gal/centros/zonapontevedrad6/aulavirtual2/file.php/3/bash.pdf -O curso-bash-2.pdf -o log
rm log
mv curso-bash-2.pdf $mov
echo -e "$W Descarga completa,Moviendo curso a $mov"
sleep 1
menu

elif [ $men == "3" ];then
echo -e "Ruta a mover el curso $C ($W ejemplo:$G /sdcard$C): "
read -p ">>> " mov
echo -e "$G [*] Descargando..."
echo "$G [*] Descargando..."
wget http://www.sistemasverschae.cl/acceso/sitio/manual%2520openoffice/paratorpes.pdf -O curso-bash-3.pdf -o log
rm log
mv curso-bash-2.pdf $mov
echo -e "$W Descarga completa,Moviendo curso a $mov"
sleep 1
menu

elif [[ $men == "00" || $men == "0" ]];then
clear
python asistente.py

else
echo "$R [!] ERROR escoja otra opcion"
sleep 1
menu

fi

}

menu
