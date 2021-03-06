#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:19:49 2018

@author: carmen.doroteo 
"""

import EntradaSalida as es

convertidor = int(input("    Idioma del convertidor    \n         1. Español \n         2. Inglés \n\n"
                            "Ingrese el idioma deseado: "))
        
if convertidor == 1:
    print("--------------------------------------------------------")
    io = es.InputOutput('NomEsp.csv')
    dframe = io.df()
#    print(dframe['Parametro'])
    """
    Esta acción imprime la columna del dataframe de los parámetros
    """
    clasificacion = int(input("   Tipo de Parámetro    \n         1. Matemático \n         2. Físico \n\n"
                            "Ingrese el Tipo de Parámetro deseado: "))
    if clasificacion == 1:
        print("--------------------------------------------------------")
        io = es.InputOutput('NomEsp.csv')
        dframe = io.df()
#        print(dframe[dframe[('Tipo_de_Parametro')] == 'Matemático'])
        """
        Esta acción imprime la columna clasificada por parámetro de tipo Matemático
        """
        propiedades = int(input("   Clasificación de los parámetros Matemáticos \n         1. Propiedades del pozo \n         2. Propiedades de la roca \n         3. Propiedades del fluido \n         4. Propiedades del yacimiento \n         5. Otros \n\n"        
                              "Ingrese el Tipo de Parámetro deseado: "))     
        if propiedades == 1:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Pozo.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Matemático'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades del pozo
            """
        if propiedades == 2:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Roca.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Matemático'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades de la roca
            """
        if propiedades == 3:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Fluido.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Matemático'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades del fluido
            """
        if propiedades == 4:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Yacimiento.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Matemático'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades del yacimiento
            """
        if propiedades == 5:
            print("--------------------------------------------------------")
            io = es.InputOutput('Otros.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Matemático'])
            """
            Esta acción imprime solamente los parámetros matemáticos que están sin clasificar
            """        
    
    if clasificacion == 2:
        print("--------------------------------------------------------")
        io = es.InputOutput('NomEsp.csv') 
        dframe = io.df()
#        print(dframe[dframe[('Tipo_de_Parametro')] == 'Físico'])
        """
        Esta acción imprime la columna clasificada por parámetro de tipo Físico
        """
        propiedades = int(input("   Clasificación de los parámetros Físicos \n         1. Propiedades del pozo \n         2. Propiedades de la roca \n         3. Propiedades del fluido \n         4. Propiedades del yacimiento \n         5. Otros \n\n"        
                              "Ingrese el Tipo de Parámetro deseado: ")) 
        if propiedades == 1:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Pozo.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Físico'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades del pozo
            """
        if propiedades == 2:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Roca.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Físico'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades de la roca
            """
        if propiedades == 3:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Fluido.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Físico'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades del fluido
            """
        if propiedades == 4:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Yacimiento.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Físico'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades del yacimiento
            """
        if propiedades == 5:
            print("--------------------------------------------------------")
            io = es.InputOutput('Otros.csv')
            dframe = io.df()
            print(dframe[dframe[('Tipo_de_Parametro')]== 'Físico'])
            """
            Esta acción imprime solamente los parámetros físicos que están sin clasificar
            """ 
        
        
elif convertidor == 2:
    print("--------------------------------------------------------")
    io = es.InputOutput('NomIng.csv')
    dframe = io.df()
#    print(dframe['Noun'])
    """
    Esta acción imprime la columna del dataframe de los parámetros
    """    
    clasificacion = int(input("   Parameter Type    \n         1. Mathematical \n         2. Physical \n\n"
                            "Enter the type of parameter required: "))
    
    if clasificacion == 1:
        print("--------------------------------------------------------")
        io = es.InputOutput('NomIng.csv')
        dframe = io.df()
#        print(dframe[dframe[('Tipo_de_Parametro')] == 'Matemático'])
        """
        Esta acción imprime la columna clasificada por parámetro de tipo Matemático
        """
        propiedades = int(input("   Classification of mathematical parameters \n         1. Properties of well \n         2. Properties of the rock \n         3. Properties of the fluid \n         4. Properties of reservoir \n         5. Others \n\n"        
                              "Enter the type of classification required: "))     
        if propiedades == 1:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Well.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Mathematical'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades del pozo
            """
        if propiedades == 2:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Rock.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Mathematical'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades de la roca
            """
        if propiedades == 3:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Fluid.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Mathematical'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades del fluido
            """
        if propiedades == 4:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Reservoir.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Mathematical'])
            """
            Esta acción imprime solamente los parámetros matemáticos de las propiedades del yacimiento
            """
        if propiedades == 5:
            print("--------------------------------------------------------")
            io = es.InputOutput('Others.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Mathematical'])
            """
            Esta acción imprime solamente los parámetros matemáticos que están sin clasificar
            """        
    
    if clasificacion == 2:
        print("--------------------------------------------------------")
        io = es.InputOutput('NomEsp.csv') 
        dframe = io.df()
#        print(dframe[dframe[('Tipo_de_Parametro')] == 'Físico'])
        """
        Esta acción imprime la columna clasificada por parámetro de tipo Físico
        """
        propiedades = int(input("   Classification of physical parameters \n         1. Properties of well \n         2. Properties of the rock \n         3. Properties of the fluid \n         4. Properties of reservoir \n         5. Others \n\n"        
                              "Enter the type of classification required: ")) 
        if propiedades == 1:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Well.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Physical'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades del pozo
            """
        if propiedades == 2:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Rock.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Physical'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades de la roca
            """
        if propiedades == 3:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Fluid.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Physical'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades del fluido
            """
        if propiedades == 4:
            print("--------------------------------------------------------")
            io = es.InputOutput('Prop_Reservoir.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Physical'])
            """
            Esta acción imprime solamente los parámetros físicos de las propiedades del yacimiento
            """
        if propiedades == 5:
            print("--------------------------------------------------------")
            io = es.InputOutput('Others.csv')
            dframe = io.df()
            print(dframe[dframe[('Parameter_Type')]== 'Physical'])
            """
            Esta acción imprime solamente los parámetros físicos que están sin clasificar
            """ 

    
else:
    print('Ingrese una opción válida')


    
#io = es.InputOutput('NomEsp.csv')
#io = es.InputOutput('NomIng.csv')

#dframe = io.df()
#print(dframe['Quantity']) 