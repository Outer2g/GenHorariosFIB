#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import urllib2
import subprocess

def initTable():
    file = open('dataQuery.dat','w+')
    file.write('<!DOCTYPE html> <html> <head> <style> table, th, td { border: 1px solid black;'+
               'border-collapse: collapse;} th, td { padding: 15px;} </style>'+
               '</head><body> <H3>Resultado de la busqueda:'+
               sys.argv[1]+' '+sys.argv[2]+'</H3><br></body></html>')
    #taula
    file.write('<table style ="width:70%">')
    file.write('<tr><th>Acte</th><th>adreca</th><th>data</th><th>transport</th></tr>')
    return file


#agafem input de fitxer
file = open('inputAssig.dat','r')
reader = csv.reader(file, delimiter=',')
url = 'https://raco.fib.upc.edu/api/horaris/horari-assignatures.txt?'
first = True
for elem in reader:
    for assig in elem:
        print assig
        if first :
            url = url + 'assignatures=GRAU-'+assig
            first = False
        url = url + '&assignatures=GRAU-'+assig

req = urllib2.Request(url)
data = urllib2.urlopen(req).read()
data = data.split('\n')
aux = []
for elem in data:
    aux.append(elem.split('\t'))
data = aux[:-1]
for elem in data:
    print elem

file = open('dataHorari.pl','w+')
for elem in data:
    #elem[0] = nom assig, elem[1]=grup, elem[2] = dia elem[3] = hora
    file.write('horari('+elem[0].lower()+','+elem[1]+','+elem[2]+','+elem[3][0]+elem[3][1]+').\n')

subprocess.call("./tratarHoraris")

file = open('horari','r')
reader = csv.reader(file,delimiter=',')
taula =initTable()