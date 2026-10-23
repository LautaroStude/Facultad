#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resolución de la guía de KNN (Iris) 
siguiendo el formato y estilo del ejemplo de diabetes.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.inspection import DecisionBoundaryDisplay

#%% 1. Cargar el dataset y mostrar las primeras filas
iris = load_iris(as_frame=True)
df_iris = iris.frame
print("Primeras filas del dataset:")
print(df_iris.head())

#%% X atributos, y etiqueta (4 atributos)
X = df_iris[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].values
y = df_iris['target'].values

#%% para usar solo 2 atributos (largo y ancho del pétalo)
X2 = df_iris[['petal length (cm)', 'petal width (cm)']].values

#%% 2. gráfico de dispersión
plt.figure(figsize=(6, 4))
plt.scatter(X2[:, 0], X2[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.xlabel('Largo del pétalo (cm)')
plt.ylabel('Ancho del pétalo (cm)')
plt.title('Distribución de los datos: Largo vs Ancho del pétalo')
plt.show()

#%% 3. construyo y ajusto el clasificador probando distintos k
print("\n--- Midiendo accuracy ---")
valores_k = [1, 3, 5, 10, 20]

for k in valores_k:
    # Entrenando con 4 atributos
    clasificador_4 = KNeighborsClassifier(n_neighbors=k)
    clasificador_4.fit(X, y)
    acc_4 = accuracy_score(y, clasificador_4.predict(X))
    
    # Entrenando con 2 atributos
    clasificador_2 = KNeighborsClassifier(n_neighbors=k)
    clasificador_2.fit(X2, y)
    acc_2 = accuracy_score(y, clasificador_2.predict(X2))
    
    print(f"k={k:2d} | Exactitud (4 attr): {acc_4:.4f} | Exactitud (2 attr): {acc_2:.4f}")

#%% 4. Elegir un valor de k (ejemplo: k=5) y entrenar el final
clasificador_final = KNeighborsClassifier(n_neighbors=5)
clasificador_final.fit(X2, y)

#%% 4a. Visualizar la frontera de decisión
plt.figure(figsize=(6, 4))
disp = DecisionBoundaryDisplay.from_estimator(
    clasificador_final, X2, response_method="predict", 
    alpha=0.5, cmap='viridis'
)
disp.ax_.scatter(X2[:, 0], X2[:, 1], c=y, edgecolor="k", cmap='viridis')
plt.xlabel('Largo del pétalo (cm)')
plt.ylabel('Ancho del pétalo (cm)')
plt.title("Frontera de decisión con k=5")
plt.show()

#%% 4b. predicción para una nueva flor
nueva_flor = [[4.8, 1.5]] 
prediccion = clasificador_final.predict(nueva_flor)

especies = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
print("\nPredicción para la nueva flor (largo 4.8, ancho 1.5):", especies[prediccion[0]])
#%%