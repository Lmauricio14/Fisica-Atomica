# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:12:41 2023

@author: DELL
"""

import numpy as numpy

#parametros (momento angular) 

#j1= float(input("Escribe el valor de j1: "))
#j2= float(input("Escribe el valor de j2: "))
#J= float(input("Escribe el valor de J: "))
j1=1
j2=1/2
J=3/2

#condición del triángulo para j
if (J < abs(j1-j2) or J > j1+j2):
    raise Exception("Ingrese valores que cumplan con la condición: |j1-j2|<=J<=j1+j2.")
    
#designando como s al eigenvalor que corresponde al operador del momento angular del sistema S
def s(m1, m2):
    return -numpy.sqrt((j2*(j2+1)-m2*(m2+1))/(j1*(j1+1)-m1*(m1-1)))

#crear la matriz para m1 m2 M CG
m1_len = int(2*j1+1)
m2_len = int(2*j2+1)
M_len = int(2*J+1)
CG = numpy.zeros((m1_len,m2_len,M_len))

#Calcular el valor de clebschGordan(j1,j1,j2,J-j1|JJ)
#partiendo de m1=j1 podemos obtener m2->J-j1 
szum = 1
ci = 1
for i in range(m1_len):
    m1 = j1-i
    m2 = J-m1
    if m2 < j2:
        ci = ci * s(m1,m2)**2
        szum = ci + szum
c = numpy.sqrt(1/szum)
m1_ind = int(j1 + j1)      #m1 = j1 
m2_ind = int(J - j1 + j2)  #m2 = J-j1
M_ind = int(J + J)
CG[m1_ind][m2_ind][M_ind] = c

#Calculamos todos los coef de clebschGordan (j1, m1, j2, m2 | JJ)
#el valor inicial es m1=j1 y m2=J-j1
for i in range(m1_len):
    m1 = j1-i
    m2 = J-m1
    m1_ind = int(m1 + j1)
    m2_ind = int(m2 + j2)
    M_ind = int(J + J)
    if (m2+1) <= j2:
        CG[m1_ind-1][m2_ind+1][M_ind] = s(m1,m2) * CG[m1_ind][m2_ind][M_ind]

#Se va restando el valor de M en 1 y se obtienen
# todas las combinaciones posibles m1,m2 para cada paso.
for iM in range(M_len-1):
    M=J-iM
    M_ind = int(M + J)
    if M_len > 1:
        for i in range(m1_len):
            m1 = j1-i
            m2 = M-m1-1
            m1_ind = int(m1 + j1)
            m2_ind = int(m2 + j2)
            if m2 <= j2:
                if abs(m1+1) > j1:
                    C1 = 0
                else:
                    C1 = numpy.sqrt(j1*(j1+1)-m1*(m1+1))/numpy.sqrt(J*(J+1)-M*(M-1))*CG[m1_ind+1][m2_ind][M_ind]
                if abs(m2+1) > j2:
                    C2 = 0
                else:
                    C2 = numpy.sqrt(j2*(j2+1)-m2*(m2+1))/numpy.sqrt(J*(J+1)-M*(M-1))*CG[m1_ind][m2_ind+1][M_ind]
                CG[m1_ind][m2_ind][M_ind-1] = C1 + C2
                
#Tabla de Clebsch-gordan        
print('j1=' + str(j1) + '   , j2=' + str(j2) + '   , J=' + str(J))
print('M       m1        m2             C')
for M_ind in range(M_len):
    M = M_ind - J
    for m1_ind in range(m1_len):
        m1 = m1_ind - j1
        for m2_ind in range(m2_len):
            m2 = m2_ind - j2
            C = CG[m1_ind][m2_ind][M_ind]
            if abs(C) > 10**(-6):
                print(M,'   ',m1,'   ',m2,'     ',C)
