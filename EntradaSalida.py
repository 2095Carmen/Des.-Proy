#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:23:08 2018

@author: carmen.doroteo
"""
import pandas as pd

class InputOutput():
    
    def __init__(self, filename):
        """
        Este es el constructor de la clase y servirá como un módulo
        para importarlo posteriormente ....
        """
        self.__df = pd.read_csv(filename, sep=',')
          
    def __del__(self):
        """
        Este es el destructor y servirá para no almacenar datos ....
        """
        del(self.__df)
        
    def df (self):
        """
        Regresa la etiqueta del DataFrame y permite la lectura 
        del archivo....
        """
        return self.__df        
    
if __name__=='__main__':
    io = InputOutput('NomEsp.csv')
#    io = InputOutput('NomenclaturaEspaniolLatex.csv')   
    dframe = io.df()
    print(dframe['Descripcion'])   
   

      
        
        
        