#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:10:06 2026

@author: lautarostude
"""
#%%
import pandas as pd
import duckdb as dd
import matplotlib.pyplot as plt
import numpy as np
#%%
carpeta = "/Users/lautarostude/Facultad/2do_año/Labo_de_datos/Archivos TP-02-20261020/"
imagenes = pd.read_csv(carpeta + "imagenes.csv")

#%%
#Cargar varias imagenes de casas
query = """
            SELECT * 
            FROM imagenes 
            WHERE label =  9
        """

imagenes_casa = dd.sql(query).df()
#imagen 3 con forma de casa
for i in range(30):
    img_casa = np.array(imagenes_casa.iloc[i, 1:]).reshape((28, 28))
    plt.imshow(img_casa, cmap='gray')
    plt.show()
#%%%
#Cargar imagenes de estrellas
query = """
            SELECT * 
            FROM imagenes 
            WHERE label =  6
        """

imagenes_estrella = dd.sql(query).df()
#imagen 3 con forma de estrella
for i in range(30):
    img_estrella = np.array(imagenes_estrella.iloc[i, 1:]).reshape((28, 28))
    plt.imshow(img_estrella, cmap='gray')
    plt.show()
#%%
#Cargar imagenes de cuadrados
query = """
            SELECT * 
            FROM imagenes 
            WHERE label =  2
        """

imagenes_cuadrado = dd.sql(query).df()
#imagen 3 con forma de cuadrado
for i in range(30):
    img_cuadrado = np.array(imagenes_cuadrado.iloc[i, 1:]).reshape((28, 28))
    plt.imshow(img_cuadrado, cmap='gray')
    plt.show()

#%%
#Cargar imagenes de peces
query = """
            SELECT * 
            FROM imagenes 
            WHERE label =  3
        """
imagenes_peces = dd.sql(query).df()
for i in range(30):
    img_pez = np.array(imagenes_peces.iloc[i, 1:]).reshape((28, 28))
    plt.imshow(img_pez, cmap='gray')
    plt.show()
    

#%%
#Cargar cualquier imagen
img = np.array(imagenes.iloc[26, 1:]).reshape((28, 28))
plt.imshow(img, cmap='gray')
plt.show()