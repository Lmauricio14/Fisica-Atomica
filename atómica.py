#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 02:04:39 2023

@author: lagarto
"""

import numpy as np
import matplotlib.pyplot as plt

nivener, masapart, Epart, cuadra, Evarias = [], [], [], [], []
nivenerpls = []
hbar = 1.05e-34
def nivelenergetico(numpart, nivener):
    for i in range (0, numpart):
        y = int(input("Ingrese el nivel energético de la %d-ésima partícula: " %int(i+1) ))
        nivener.append(y)
    return nivener

def nivelenergeticosumado(numpart, nivener, nivenerpls,potenciador):
    for i in range (0, numpart):
        xyz = nivener[i]+potenciador 
        nivenerpls.append(xyz)
    return nivenerpls

def sumanivelescua(numpart, nivener):
    yyy = 0
    for i in range (0, numpart):
        yyy = nivener[i]**2  + yyy
    return yyy

def masaparticula(numpart, masapart):
    for i in range (0, numpart):
        x = float(input("Ingrese la masa (en Kilogramos) de la %d-ésima partícula: " %int(i+1) ))
        masapart.append(x)
    return masapart

def componenteE(numpart, masapart, nivener):
    for i in range (0, numpart):
        zz = (nivener[i]**2)/(masapart[i])
        Epart.append(zz)
    return Epart

def EnergiaTotal(numpart, masapart, nivener, factorE):
    masaparts = masaparticula(numpart, masapart)
    nivelenergia = nivelenergetico(numpart, nivener)
    cuadra = sumanivelescua(numpart, nivener)
    Epart = componenteE(numpart, masaparts, nivelenergia)
    sumaenergia = 0
    for i in range(0, numpart):
        sumaenergia = sumaenergia + Epart[i]
    energiatotal = factorE*sumaenergia
    return energiatotal, cuadra



numpart = int(input("Ingrese el número de partículas: "))

L = float(input("Ingrese la longitud de la caja unidimensional (En Metros): "))

factorE = ((np.pi**2)*hbar**2)/(2*(L**2))

Etotal,nivelcuad = EnergiaTotal(numpart, masapart, nivener, factorE)



print("La energía total para el sistema es de", Etotal, "Joules")




plt.scatter(cuadra, Evarias, s=900, marker="_", linewidth=2, zorder=3)
plt.show()
