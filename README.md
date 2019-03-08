# yassPing
PREFAZIONE
Usando la libreria "pythonping" questo script necessita che l'utente sia root o che abbia i permessi sufficenti sui socket.

USO: yassPing ip
ESEMPIO: yassPing 192.168.1.1
  
Questo comando "pinga" l'ip passato come parametro fino alla pressione di CTRL-C

Cosa cambia da un comunissimo ping allora?
1. Il ping non mi dice quando un pacchetto viene perso (linux), semplicemente l’icmp_seq salta la sequenza per quanti pacchetti non tornano
2. il ping tradizionale non da evidenza ne a che ora ne quanti ne quanti pacchetti di fila vengono persi (1000 pacchetti su 1 milione: perderne 1 ogni 1000 è diverso che 1000 di fila!)
