#!/usr/bin/python3

from pythonping import ping
from time import sleep
from datetime import datetime
import sys
import ipaddress
import os

def checkIP(ip):
    try:
        ipaddress.ip_address(ip)
        return False
    except:
        return True


def stats(errori, i):
    print('\nStatistiche')
    print('-----------')
    print('Pacchetti inviati: ' + str(i))
    print('Pacchetti persi: ' + str(len(errori)))
    for e in errori:
        print('ERRORE: ' + str(e))

if __name__ == '__main__':
    if os.geteuid() == 0:
        if len(sys.argv) != 2 or checkIP(sys.argv[1]):
            print('\nUSO: yassPing <indirizzoIP>')
            print('ESEMPIO:')
            print('yassPing 192.168.1.1')
        else:
            ip = sys.argv[1]
            errori = []
            i = 0
            while True:
                i += 1
                try:
                    dataPing = datetime.now().strftime('%H:%M:%S')
                    r = ping(str(ip), count=1, timeout=1)
                    if r.rtt_max >= 1:
                        print(str(dataPing) + ' !!! PACCHETTO PERSO !!!')
                        errori.append(dataPing)
                    else:
                        print(str(dataPing) + ' [' + str(i) + '] VERSO: ' + str(ip) + ' TEMPO: ' + str(r.rtt_max))
                        sleep(1)
                except KeyboardInterrupt:
                    stats(errori, i)
                    sys.exit(0)

            stats(errori, i)
    else:
        print('\nDevi essere root per eseguire questo stupido script')