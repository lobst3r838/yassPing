# yassPing
PREFAZIONE
La libreria "pythonping" crea un socket e di conseguenza questo script necessita che l'utente sia root o che abbia i permessi socket.

USO: yassPing <indirizzoIP> <numero pacchetti>'
ESEMPIO: yassPing 192.168.1.1 100
  
Questo comando lancia 100 ping verso l'ip 192.168.1.1

Cosa cambia da un comunissimo ping allora?
In primo luogo, in caso di pacchetto perso (o con RTT > 1sec) lo script avvisa del pacchetto perso, in secondo luogo o al termine dell'esecuzione o in caso di interruzione (CTRL+C) lo script riepiloga quanti pacchetti sono andati persi e a che orario.
