#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:19:49 2018

@author: carmen.doroteo 
"""

import EntradaSalida as es


Convertidor = int(input("    Idioma del convertidor    \n         1. Español \n         2. Inglés \n\n"
                            "Ingrese el idioma deseado: "))
        
if Convertidor == 1:
    print("--------------------------------------------------------")
    io = es.InputOutput('NomEsp.csv')
    dframe = io.df()
    clasificacion =  int(input("1. Matematica \n 2. Fisica \n\n Ingrese: "))
    if clasificacion == 1:
        print
    elif clasificacion == 2:
        asdadsa
        
#    print(dframe.iloc[0])
#    print(dframe['Clasificacion'])
    
elif Convertidor == 2:
    print("--------------------------------------------------------")
    io = es.InputOutput('NomIng.csv')
    dframe = io.df()
    print(dframe['Quantity'])
    
#else:
#    return Convertidor():
#    print('Ingrese una opción válida')


    
#io = es.InputOutput('NomEsp.csv')
#io = es.InputOutput('NomIng.csv')

#dframe = io.df()
#print(dframe['Quantity']) 